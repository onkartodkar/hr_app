from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('notification_list/', views.NotificationList.as_view(), name='notification_list'),
    path('mark_as_read/<int:notification_id>/', views.NotificationMarkAsRead.as_view(), name='mark_as_read'),
]

