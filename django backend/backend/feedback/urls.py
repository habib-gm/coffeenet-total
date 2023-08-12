from django.urls import path
from . import views

urlpatterns = [path("api/send-feedback/", views.createFeedback)]
