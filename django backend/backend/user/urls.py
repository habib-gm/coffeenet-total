from . import views
from django.urls import path

urlpatterns = [
    path("api/register/", views.createUser),
    path("api/get-curr-user/", views.getCurrUser),
    path("api/change-password/", views.updatePassword),
]
