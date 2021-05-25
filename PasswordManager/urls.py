from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addsite', views.addsite, name='addsite'),
    path('viewallsites', views.viewallsites ,name='viewallsites'),
    path('addDocument', views.addDocument, name='addDocument'),
    path('GenPass', views.GenPass, name='GenPass'),
    path('deleteDoc', views.deleteDoc, name='deleteDoc'),
    path('deletePass', views.deletePass, name='deletePass'),
    # path('downloadFile', views.downloadFile, name='downloadFile'),

]
