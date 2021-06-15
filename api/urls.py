from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name ="home"),
    path('upload/',views.uploadResume,name="upload"),
    path('successUpload/',views.successUpload,name ='successUpload'),
    path('viewResume/',views.viewResume,name = "viewResume"),
    path('getApi/',views.getApi,name ='getApi'),
    path('apiId/<str:pk>/',views.apiId,name ='apiId'),
    path('getXls/',views.getXls,name = 'getXls'),
]
