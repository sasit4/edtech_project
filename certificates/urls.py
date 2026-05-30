<<<<<<< HEAD
from django.urls import path
from .views import generate_certificate

urlpatterns = [

    path('', generate_certificate, name='certificate'),

=======
from django.urls import path
from .views import generate_certificate

urlpatterns = [

    path('', generate_certificate, name='certificate'),

>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
]