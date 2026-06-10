
from django.urls import path
from .views import *

urlpatterns=[

    path('<int:id>/',quiz_page,name='quiz_page'),

    path('result/<int:id>/',quiz_result,name='quiz_result'),

    path('leaderboard/',leaderboard,name='leaderboard'),

]