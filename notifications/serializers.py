from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created_at_time = serializers.SerializerMethodField()

    def get_created_at_time(self, instance):
        created_at_time = instance.created_at_time.strftime("%Y-%m-%d")
        return created_at_time

    class Meta:
        model = Notification
        fields = '__all__'
