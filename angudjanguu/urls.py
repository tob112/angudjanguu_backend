"""angudjanguu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework import routers
from angudjanguu import settings
from rest_framework.authtoken import views

from authentication import views

router = routers.SimpleRouter()
router.register(r'users', views.UserListViewset)

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include(router.urls)),

    url(r'^api/v1/auth/', include('rest_auth.urls')),

    url(r'^api-token-auth/', views.obtain_auth_token)

    # url(r'^api/v1/auth/', include(router.urls)),
    # password/reset
    # password/reset/confirm
    # login
    # logout
    # user
    # password

]
