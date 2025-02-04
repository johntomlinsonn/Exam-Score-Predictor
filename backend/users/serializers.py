# filepath: /c:/Users/bobtt/OneDrive/Desktop/Documents/JackCS/exam-predictor/backend/users/serializers.py
from rest_framework import serializers
from .models import CustomUser, TestScore

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'study_habits']

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = ['id', 'user', 'subject', 'score', 'study_duration', 'feeling_before_test', 'mistakes_made']