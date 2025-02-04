from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

class SomeProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your code here
        pass

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
