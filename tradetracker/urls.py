from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('trades/', include('trades.urls', namespace='trades')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('charts/', include('charts.urls', namespace='charts')),
] 
