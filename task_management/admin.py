from django.contrib import admin
from .models import Users, Tasks


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Description', 'Due_Date', 'Priority_Level', 'Status', 'User', 'Completed_at')
