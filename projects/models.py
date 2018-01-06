from django.db import models
from django.utils import timezone
import operator

from requirements.models import Requirement, Assessment

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(default=timezone.now)

    stakeholders = models.ManyToManyField('clients.Client', through='Power')

    def __str__(self):
        return self.name

    def getNextReleaseFeatures(self, capacity):
        requirementsObjects = Requirement.objects.all().filter(project=self).filter(state=False)
        requirements = {}
        for requirement in requirementsObjects:
            requirement.last_released = False
            requirement.save()
            requirements[requirement.id] = requirement.benefit
        sortedRequirements = reversed(sorted(requirements.items(), key=operator.itemgetter(1)))

        requirementsRelease = []
        sum=0
        for requirement in sortedRequirements:
            req = requirementsObjects.get(id=requirement[0])
            if (sum + req.effort <= int(capacity)):
                sum = sum + req.effort
                requirementsRelease.append(req.id)
                req.last_released = True
            req.save()

        return Requirement.objects.filter(id__in=requirementsRelease)

    def checkFillables(self):
        bad_influencies = []
        influencies = Power.objects.all().filter(project=self.id)
        for inf in influencies:
            if not inf.weight:
                bad_influencies.append(inf.client.name)

        bad_assesments = []
        assesments = Assessment.objects.all().filter(requirement__in=Requirement.objects.filter(project=self))
        for assesment in assesments:
            if not assesment.value:
                bad_assesments.append(assesment)

        return True, bad_influencies, bad_assesments

class Power(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.client.name+" weight in project "+self.project.name
