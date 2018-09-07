from . import views
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account, name="my_account"),
]
