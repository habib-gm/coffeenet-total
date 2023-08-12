from django.urls import path
from . import views

urlpatterns = [
    path("api/predict/", views.predict),
    path("api/predict/get-data/", views.getAllData),
]
