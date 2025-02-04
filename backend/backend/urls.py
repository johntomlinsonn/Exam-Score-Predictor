# filepath: /c:/Users/bobtt/OneDrive/Desktop/Documents/JackCS/exam-predictor/backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet, TestScoreViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'test-scores', TestScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(router.urls)),
]