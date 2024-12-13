from django.urls import path
from emails.views import onboarding, utility

app_name = 'emails'

urlpatterns = [
    path('send_email/', onboarding.send_email, name='send_email'),
    path('get_email_templates/', utility.get_email_templates, name='get_email_templates'),
]
