from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage

from emails.models import EmailTemplate
from onboarding.models import JobApplication


def EmailForHR_candidate_status_update(data):
    subject = data['subject']
    body = data['body']
    to_emails = data['to_emails']
    cc_emails = data['cc_emails']
    bcc_emails = data['bcc_emails']

    try:
        email = EmailMessage(subject, body, to=to_emails, cc=cc_emails, bcc=bcc_emails)
        email.send()
        return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"error": "Failed to send email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def send_email(request):
    data = request.data

    try:
        # user = request.user

        # applicant_id="1"
        applicant_id = data.get("id")
        context_data = data.get("context_data", {})
        print(context_data,"context_data")
        # user_name = data.get("user_name")
        # company_name = data.get("company_name")
        applicant = JobApplication.objects.get(pk=applicant_id)

        selected_template = EmailTemplate.objects.get(name=data.get('name'), version=data.get('version',1.0))

        content_without_html_tags = selected_template.render(context_data)
        body = f'<html><body>{content_without_html_tags}</body></html>'

        subject = selected_template.subject
        to_emails = [applicant.email]
        # to_emails = data.get('to_emails', [])
        cc_emails = data.get('cc_emails', [])
        bcc_emails = data.get('bcc_emails', [])

        email = EmailMessage(subject, body, to=to_emails, cc=cc_emails, bcc=bcc_emails)
        email.content_subtype = "html"
        email.send()

        return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"error": "Failed to send email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
