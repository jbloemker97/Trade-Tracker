from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'trades'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.trades, name='add'),
    path('delete/<int:pk>', views.delete_trade, name='delete'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
]
