from django.contrib import admin
from .models import Blog
from unfold.admin import ModelAdmin

@admin.register(Blog)
class BlogClass(ModelAdmin):
	list_display = ('title', 'author') 
