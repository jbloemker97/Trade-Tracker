from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account, name='my_account'),
    path('login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
