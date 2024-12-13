from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from emails.models import EmailTemplate
# from emails.serializers import EmailSerializer
from emails.views.onboarding import EmailForHR_candidate_status_update
from notifications.serializers import NotificationSerializer
from .models import JobApplication, JobApplicationRemark, CandidateDiscussion, JobApplicationDocument, PreviousJobDetail
from .serializers import JobApplicationSerializer, JobApplicationRemarkSerializer, JobApplicationDocumentSerializer, PreviousJobDetailSerializer, CandidateDiscussionSerializer
from accounts.models import User, JobRole
from main.CONSTANTS import *


class JobApplicationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            job_application = serializer.save()

            return Response({"message": "Job application submitted successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def job_application_details(request, job_application_id):
    try:
        job_application = JobApplication.objects.get(id=job_application_id)
    except JobApplication.DoesNotExist:
        return Response({"error": "Job Application not found"}, status=404)

    try:

        remark = JobApplicationRemark.objects.get(application=job_application)
        discussion = CandidateDiscussion.objects.get(application=job_application)
        document = JobApplicationDocument.objects.get(application=job_application)
        previous_job_details = PreviousJobDetail.objects.get(application=job_application)

        job_serializer = JobApplicationSerializer(job_application)
        discussion_serializer = CandidateDiscussionSerializer(discussion)
        document_serializer = JobApplicationDocumentSerializer(document)
        previous_job_serializer = PreviousJobDetailSerializer(previous_job_details)
        remark_serializer = JobApplicationRemarkSerializer(remark)
    except Exception as e:
        print(e)

    data = {
        "job_application": job_serializer.data,
        "remark": remark_serializer.data,
        "discussion": discussion_serializer.data,
        "document": document_serializer.data,
        "previous_jobs": previous_job_serializer.data,
    }

    return Response(data)


@api_view(['GET'])
def job_application_list(request):
    job_applications = JobApplication.objects.all()
    serializer = JobApplicationSerializer(job_applications, many=True)
    return Response(serializer.data)


class JobApplicationUpdateStatus(APIView):
    def post(self, request, application_id, *args, **kwargs):
        try:
            print(application_id)
            job_application = JobApplication.objects.get(pk=int(application_id))
            print(job_application)
        except JobApplication.DoesNotExist:
            return Response({"error": "Job application not found."}, status=status.HTTP_404_NOT_FOUND)

        status_value = request.data.get('status')
        remark_content = request.data.get('remark')
        generated_by = request.data.get('user')

        if not status_value or not remark_content:
            return Response({"error": "Both 'status' and 'remark' are required in the request data."},
                            status=status.HTTP_400_BAD_REQUEST)

        job_application.application_status = status_value
        job_application.save()
        job_role = JobRole.objects.get(title='HR_HOD')

        hr_hod_user = User.objects.filter(job_role=job_role).first()

        remark_data = {
            'application': job_application.id,
            'generated_by': int(generated_by),
            'receiver': hr_hod_user.id if hr_hod_user else None,
            'message': remark_content,
        }

        remark_serializer = NotificationSerializer(data=remark_data)
        if remark_serializer.is_valid():
            remark_serializer.save()
            # print(remark_serializer.data)
        else:
            print(remark_serializer.errors)
            return Response({"error": "Failed to create a remark."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        email_template = EmailTemplate.objects.get(name='Onboarding', version='1.0')
        email_context = {'application_id': job_application.id, 'status': status_value, 'remark': remark_content}
        email_subject = email_template.render({'status': status_value})
        email_body = email_template.render(email_context)

        email_data = {
            'subject': email_subject,
            'body': email_body,
            'to_emails': [hr_hod_user.email],
            'cc_emails': [standard_bcc_mail],
            'bcc_emails': [standard_bcc_mail],
        }

        email_response = EmailForHR_candidate_status_update(email_data)

        if email_response.status_code != status.HTTP_200_OK:
            return Response({"error": "Failed to send email."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Application status updated successfully and email sent."},
                        status=status.HTTP_200_OK)


@api_view(['POST'])
def add_documents(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        application_id = data.get('application_id')
        doc_type = data.get('doc_type')
        # application=JobApplication.objects.get(pk=application_id)

        try:
            application = JobApplication.objects.get(pk=application_id)
        except JobApplication.DoesNotExist:
            return Response({"error": "Job application does not exist"}, status=status.HTTP_404_NOT_FOUND)

            # Assuming 'file' is coming from request.FILES
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        new_document = JobApplicationDocument.objects.create(
            application=application,
            type=doc_type,
            file=file
        )
        serialized_new_document = JobApplicationDocumentSerializer(new_document, context={'request': request})
        print(serialized_new_document.data)

        return Response({"success": serialized_new_document.data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def delete_document(request):
    if request.method == "POST":
        data = request.data
        print(data)
        document_id = data.get('document_id')
        print(document_id)

        try:
            document = JobApplicationDocument.objects.get(pk=document_id)
        except JobApplicationDocument.DoesNotExist:
            return Response({"error": "Document does not exist"}, status=405)

        document.delete()
        return Response({"success": "Document deleted successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def edit_document(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        document_id = data.get('document_id')
        new_doc_type = data.get('new_doc_type')
        new_file = request.FILES.get('new_file')

        try:
            document = JobApplicationDocument.objects.get(pk=document_id)
        except JobApplicationDocument.DoesNotExist:
            return Response({"error": "Document does not exist"}, status=status.HTTP_404_NOT_FOUND)
        document.type = new_doc_type
        if new_file:
            document.file = new_file

        document.save()

        serialized_document = JobApplicationDocumentSerializer(document, context={'request': request})
        return Response({"success": serialized_document.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_applicant_documents(request, applicant_id):
    if request.method == "GET":
        try:
            applicant = JobApplication.objects.get(pk=applicant_id)
        except JobApplication.DoesNotExist:
            return Response({"error": "Applicant does not exist"}, status=status.HTTP_404_NOT_FOUND)

        documents = JobApplicationDocument.objects.filter(application=applicant)

        serialized_documents = JobApplicationDocumentSerializer(documents, many=True, context={'request': request})
        return Response({"success": serialized_documents.data}, status=status.HTTP_200_OK)


def get_document_details(request, document_id):
    document = get_object_or_404(JobApplicationDocument, pk=document_id)
    serialized_document = JobApplicationDocumentSerializer(document)
    return JsonResponse({"success": serialized_document.data})