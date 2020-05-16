"""writemydiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from diary.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing),
    path("signin/", signin),
    path("signup/", signup),
    path("dashboard/",dashboard),
    path("diary/<int:DiaryEntries_id>/",diary_specific),
    path("edit/<int:DiaryEntries_id>/", edit_diary),
    path("create/",create_diary),
    path("fav/<int:DiaryEntries_id>/", addToFavourites),
    path("unfav/<int:DiaryEntries_id>/", unFavourite),
    path("deleteDiary/<int:DiaryEntries_id>/", delete_diary),
    path("faq/",faq),
    path("feedback/",feedback),
    path("fav-diaries/", starred),
    path("signout/",signout),
    path("contact/",contact)
]
