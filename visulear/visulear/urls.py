"""visulear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views
from voca import views as voca_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('auth/', include('social_django.urls', namespace = 'social')),
    path('', voca_views.home, name = 'home'),
    path('vocab_part/<int:tSid>/', voca_views.vocab, name='vocab'),
    path('save/<int:qid>/', voca_views.saveVocab),
    path('result/<int:tSid>/', voca_views.result, name='result')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)