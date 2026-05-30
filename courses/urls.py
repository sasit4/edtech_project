from django.urls import path
from .views import *

urlpatterns = [

    path('', course_list, name='courses'),

    path('enroll/<int:id>/', enroll_course, name='enroll_course'),

    path('watch/<int:id>/', watch_course, name='watch_course'),

    path('<int:id>/', course_details, name='course_details'),

]