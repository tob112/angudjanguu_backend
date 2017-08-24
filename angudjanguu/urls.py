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
from rest_framework_jwt.views import obtain_jwt_token
from authentication import views
from analysis import views as analysisviews
from rest_framework_jwt.views import refresh_jwt_token

from kicker.views import TeamViewset, MatchViewset, PlayaViewset

router = routers.SimpleRouter()
router.register(r'users', views.UserListViewset)

router.register(r'analysis', analysisviews.AnalysisViewset)
router.register(r'vectors', analysisviews.VectorViewset)
router.register(r'messgroessen', analysisviews.MessgroesseViewset)

router.register(r'teams', TeamViewset)
router.register(r'matches', MatchViewset)
router.register(r'kicker_profiles', PlayaViewset)

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/login/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),

    url(r'^api/v1/auth/', include('rest_auth.urls')),

    # url(r'^api-token-auth/', views.obtain_auth_token)

    # url(r'^api/v1/auth/', include(router.urls)),
    # password/reset
    # password/reset/confirm
    # login
    # logout
    # user
    # password

]
