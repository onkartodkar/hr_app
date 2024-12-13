from django.db import models
from accounts.models import User
from django.template import Context, Template
from django.core.mail import EmailMessage


class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        unique_together = ['name', 'version']

    def render(self, context_data):
        template = Template(self.body)
        context = Context(context_data)
        return template.render(context)

    def __str__(self):
        return self.name


class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    cc = models.CharField(max_length=255, blank=True, null=True)
    bcc = models.CharField(max_length=255, blank=True, null=True)
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, null=True, blank=True)
    context_data = models.JSONField(null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def send(self):
        subject = self.template.render(self.context_data)
        body = self.template.render(self.context_data)

        email = EmailMessage(subject, body, to=[self.recipient.email])
        email.send()

        self.is_sent = True
        self.save()

    def __str__(self):
        return self.sender.email
