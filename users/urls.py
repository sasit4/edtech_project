<<<<<<< HEAD
from django.urls import path
from .views import *
from . import views

urlpatterns=[

    path('register/',register_user,name='register'),

    path('login/',login_user,name='login'),

    path('logout/',logout_user,name='logout'),

    path('dashboard/',dashboard,name='dashboard'),

    path('profile/',profile,name='profile'),

   path('edit-profile/', views.edit_profile, name='edit_profile')
=======
from django.urls import path
from .views import *
from . import views

urlpatterns=[

    path('register/',register_user,name='register'),

    path('login/',login_user,name='login'),

    path('logout/',logout_user,name='logout'),

    path('dashboard/',dashboard,name='dashboard'),

    path('profile/',profile,name='profile'),

   path('edit-profile/', views.edit_profile, name='edit_profile')
>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
]