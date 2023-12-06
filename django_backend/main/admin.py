from django.contrib import admin
from .models import WorkshopTeamStatus,User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
