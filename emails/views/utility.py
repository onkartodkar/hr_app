from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from emails.models import EmailTemplate
from emails.serializers import EmailTemplateSerializer


@api_view(['GET'])
def get_email_templates(request):
    try:
        welcome_template = EmailTemplate.objects.all()
        serializer = EmailTemplateSerializer(welcome_template, many=True)
        return Response({"success": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": "Failed to fetch templates."}, status=status.HTTP_400_BAD_REQUEST)
