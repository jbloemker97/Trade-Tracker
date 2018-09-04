from . import views
from django.urls import path

app_name = 'trades'
urlpatterns = [
    path('register/', views.register, name='register'),
]
