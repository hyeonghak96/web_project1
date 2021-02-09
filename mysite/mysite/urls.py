"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
<<<<<<< HEAD
from mysite.views import HomeView, Profile, UserCreateView, UserCreateDoneTV
=======
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
>>>>>>> ed109dacdff747269a167d6bbf6367b9a538d12b
from django.urls import path

# from instrouction.views import InstrouctionLV, InstrouctionDV
from mysite.views import HomeView, InstrouctionIntroView, InstrouctionPlanView, InstrouctionStructureView, InstrouctionView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('account/', include('django.contrib.auth.urls')), # 로그인, 로그아웃, 비밀번호 변경 등 담당
    
    
    path('account/register/', UserCreateView.as_view(), name='register'), 
    path('account/register/done/', UserCreateDoneTV.as_view(),name='register_done'), # 회원 가입 및 처리
<<<<<<< HEAD
    path('assessment/', include('assessment.urls')), #평가 url
=======
>>>>>>> ed109dacdff747269a167d6bbf6367b9a538d12b
    path('instrouction/',InstrouctionView.as_view(), name='instrouctionbase'),
    path('instrouction/intro',InstrouctionIntroView.as_view(), name ='intro'),
    path('instrouction/structure',InstrouctionStructureView.as_view(), name ='structure'),
    path('instrouction/plan',InstrouctionPlanView.as_view(), name ='plan'),
<<<<<<< HEAD
    path('account/profile',Profile.as_view(), name ='profile'),
=======



    path('assessment/', include('assessment.urls')), #평가 url


    
>>>>>>> ed109dacdff747269a167d6bbf6367b9a538d12b


    
    path('instrouction/',include('instrouction.urls')),
<<<<<<< HEAD
=======

    path('blog/',include('blog.urls')),
>>>>>>> ed109dacdff747269a167d6bbf6367b9a538d12b
]
