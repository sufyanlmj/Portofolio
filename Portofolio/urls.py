
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static as django_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saya.urls')),
]

if settings.DEBUG:
    urlpatterns += django_static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += django_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)