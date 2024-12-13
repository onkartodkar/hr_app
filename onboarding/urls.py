from django.urls import path
from . import views

app_name = 'onboarding'

urlpatterns = [
    path('application/', views.JobApplicationView.as_view(), name='job_application_api'),
    # path('add_documents/', views.add_documents, name='add_documents'),
    path('applications_received/', views.job_application_list, name='job_application_list'),
    path('applications_details/<int:job_application_id>/', views.job_application_details,
         name='job_application_details'),
    path('job_application_update_status/<int:application_id>/', views.JobApplicationUpdateStatus.as_view(),
         name='job_application_update_status'),

    path('add_documents/', views.add_documents, name='add_documents'),
    path('edit_document/', views.edit_document, name='edit_document'),
    path('delete_document/', views.delete_document, name='delete_document'),
    path('get_applicant_documents/<int:applicant_id>/', views.get_applicant_documents, name='get_applicant_documents'),
    path('get_document_details/<int:document_id>/', views.get_document_details, name='get_document_details'),

]
