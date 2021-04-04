from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('api/v1/calculate/',views.SeriesAPI.as_view(),name='post-view')
]
