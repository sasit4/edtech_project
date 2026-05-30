<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns=[

    path('<int:id>/',quiz_page,name='quiz_page'),

    path('result/<int:id>/',quiz_result,name='quiz_result'),

    path('leaderboard/',leaderboard,name='leaderboard'),

=======
from django.urls import path
from .views import *

urlpatterns=[

    path('<int:id>/',quiz_page,name='quiz_page'),

    path('result/<int:id>/',quiz_result,name='quiz_result'),

    path('leaderboard/',leaderboard,name='leaderboard'),

>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
]