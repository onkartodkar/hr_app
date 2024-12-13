from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onboarding.urls'), name='onboarding'),
    path('', include('notifications.urls'), name='notifications'),
    path('', include('emails.urls'), name='emails'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)