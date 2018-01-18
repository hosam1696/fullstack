from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('detail/', views.detail, name='detail'),
    path('$', views.Notfound, name='404')
]