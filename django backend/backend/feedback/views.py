from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.response import Response

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createFeedback(request):
    data = request.data
    user = request.user
    subject = data.get("subject", "")
    content = data.get("content", "")
    try:
        Feedback.objects.create(user=user, content=content, subject=subject)
    except Exception as e:
        print(e)
        return Response(status=500)
    return Response(status=200)
