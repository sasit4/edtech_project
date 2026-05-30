<<<<<<< HEAD
"""
URL configuration for language_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('users/',include('users.urls')),
    path('courses/',include('courses.urls')),
    path('quiz/',include('quiz.urls')),
    path('certificate/', include('certificates.urls')),
    path('users/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
=======
"""
URL configuration for language_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('users/',include('users.urls')),
    path('courses/',include('courses.urls')),
    path('quiz/',include('quiz.urls')),
    path('certificate/', include('certificates.urls')),
    path('users/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
document_root=settings.MEDIA_ROOT)