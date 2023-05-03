import django.conf.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', django.conf.urls.include('gestioncours.urls')),
    path('', django.conf.urls.include('gestioncours.urls')),
    path('', include("django.contrib.auth.urls")),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
