from . import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account, name='my_account'),
    path('login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
]
