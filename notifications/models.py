from django.db import models
from django.utils import timezone
from accounts.models import User
from onboarding.models import JobApplication


class Notification(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, blank=True)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    message = models.TextField()
    created_at_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    read_at_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at_time']

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at_time = timezone.now()
            self.save()

    def __str__(self):
        return self.generated_by.user_name
