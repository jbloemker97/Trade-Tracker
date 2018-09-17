from . import views
from django.urls import path

app_name = 'charts'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('data/', views.get_data, name='charts')
]
