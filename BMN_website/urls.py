from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('BMN.urls')),
    # Other URL patterns if needed
    path('admin/', admin.site.urls),
]
