from . import views
from django.urls import path

app_name = 'charts'
urlpatterns = [
    path('charts/', views.get_data, name='charts')
]
