<<<<<<< HEAD
from django.contrib import admin
from .models import Course, Category
# Register your models here.

class CouresAdmin(admin.ModelAdmin):
    list_display=['title','instructor','price']
    admin.site.register(Category)
=======
from django.contrib import admin
from .models import Course, Category
# Register your models here.

class CouresAdmin(admin.ModelAdmin):
    list_display=['title','instructor','price']
    admin.site.register(Category)
>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
admin.site.register(Course,CouresAdmin)