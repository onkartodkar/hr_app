from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            notifications = Notification.objects.all()
            serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
5

class NotificationMarkAsRead(APIView):
    def post(self, request, notification_id, *args, **kwargs):
        try:
            notification = Notification.objects.get(pk=notification_id)
            notification.mark_as_read()
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"error": "Error occurred"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Notification marked as read successfully."},
                        status=status.HTTP_200_OK)


