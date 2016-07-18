"""django_rest_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^rest-swagger/', schema_view),
    url(r'^blog/', blog_page),



    # Rest
    url(r'^api/blog/', blog_api.as_view()),
]