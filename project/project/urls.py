"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from home.views import NewsViewSet,HotsViewSet, CollectionViewSet, RecommendViewSet, MoreViewSet, UserViewSet, AuthView, Email_code_APIView, RegisterView,TokenAuthView, DonorViewSet, Forget_Email_code_APIView, ForgetView, DonorlinkAuthView, SearchView
from django.conf.urls import url




router = routers.DefaultRouter()
router.register(r'News', NewsViewSet)
router.register(r'Hots', HotsViewSet)
router.register(r'Collection', CollectionViewSet)
router.register(r'Recommend', RecommendViewSet)
router.register(r'more', MoreViewSet)
# router.register(r'Users', UserViewSet)
router.register(r'Donor', DonorViewSet)
# router.register(r'Donorlink', DonorlinkViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'^api/v1/auth/$', AuthView.as_view()),
    # url(r'^api/v1/token/$', TokenView.as_view()),
    url(r'^api/v1/fs/$', Email_code_APIView.as_view()),
    url(r'^api/v1/yz/$', RegisterView.as_view()),
    url(r'^api/v1/fgfs/$', Forget_Email_code_APIView.as_view()),
    url(r'^api/v1/fgyz/$', ForgetView.as_view()),
    url(r'^api/v1/TokenAuthView/$', TokenAuthView.as_view()),
    url(r'^api/v1/DonorlinkAuthView/$', DonorlinkAuthView.as_view()),
    url(r'^api/v1/SearchView/$', SearchView.as_view()),
]
