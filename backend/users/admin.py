from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TestScore

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

class TestScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'score', 'study_duration', 'feeling_before_test', 'mistakes_made']
    search_fields = ['user__username', 'subject']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TestScore, TestScoreAdmin)
