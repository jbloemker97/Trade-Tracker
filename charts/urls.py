from . import views
from django.urls import path

app_name = 'charts'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('data/', views.get_data, name='charts'),
    path('data/max_pnl/', views.get_max_pnl),
    path('data/future', views.get_future_pnl),
    path('data/wins/', views.get_winning_percentage),
]
