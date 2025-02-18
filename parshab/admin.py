from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Todolist)
class PTodolistAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed']
    list_editable = ["is_completed"]