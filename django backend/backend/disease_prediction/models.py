from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def upload_to_image(instance, filename):
    return "images/{filename}".format(filename=filename)


def upload_to_prediction(instance, filename):
    return "predictions/{filename}".format(filename=filename)


class Disease(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Prediction(models.Model):
    image = models.ImageField(upload_to=upload_to_image)
    imageName = models.CharField(max_length=30)
    diseases = models.ManyToManyField(Disease)
    scanned = models.BooleanField(default=True)
    severity = models.FloatField()
    uploadTime = models.DateTimeField(auto_now_add=True)
    predictedImage = models.ImageField(
        upload_to=upload_to_prediction, blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.imageName + "-prediction"
