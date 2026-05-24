from django.contrib import admin
from .models import Course, Category
# Register your models here.

class CouresAdmin(admin.ModelAdmin):
    list_display=['title','instructor','price']
    admin.site.register(Category)
admin.site.register(Course,CouresAdmin)