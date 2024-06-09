from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/rental/', include('rental.urls')),
    path('v1/manage/', include('adminapp.urls')),
    
]
