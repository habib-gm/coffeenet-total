from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
import os
import datetime
from datetime import timedelta


class PredictionSerializer(ModelSerializer):
    diseases = SerializerMethodField()
    originalImageSize = SerializerMethodField()
    predictedImageSize = SerializerMethodField()
    uploadTime = SerializerMethodField()

    def get_originalImageSize(self, object):
        imagePath = object.image.path
        return os.stat(imagePath).st_size

    def get_predictedImageSize(self, object):
        imagePath = object.predictedImage.path
        return os.stat(imagePath).st_size

    def get_diseases(self, object):
        diseases = object.diseases.all()
        return [disease.name for disease in diseases]
    
    def get_uploadTime(self,object:Prediction):
        time = object.uploadTime.timestamp() 
        return time

    class Meta:
        model = Prediction
        fields = [
            "imageName",
            "predictedImage",
            "diseases",
            "id",
            "image",
            "originalImageSize",
            "predictedImageSize",
            "scanned",
            "severity",
            "uploadTime",
        ]
