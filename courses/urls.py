<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns = [

    path('', course_list, name='courses'),

    path('enroll/<int:id>/', enroll_course, name='enroll_course'),

    path('watch/<int:id>/', watch_course, name='watch_course'),

    path('<int:id>/', course_details, name='course_details'),

=======
from django.urls import path
from .views import *

urlpatterns = [

    path('', course_list, name='courses'),

    path('enroll/<int:id>/', enroll_course, name='enroll_course'),

    path('watch/<int:id>/', watch_course, name='watch_course'),

    path('<int:id>/', course_details, name='course_details'),

>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
]