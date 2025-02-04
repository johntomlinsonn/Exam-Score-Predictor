from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, TestScore
from .serializers import CustomUserSerializer, TestScoreSerializer

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class TestScoreViewSet(viewsets.ModelViewSet):
    queryset = TestScore.objects.all()
    serializer_class = TestScoreSerializer
