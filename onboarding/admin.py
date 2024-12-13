from django.contrib import admin
from .models import JobApplication, JobApplicationRemark, CandidateDiscussion, JobApplicationDocument, PreviousJobDetail

# Register your models here.
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicant_name', 'email', 'phone_number', 'applied_job', 'application_status', 'created_at')
    list_filter = ('application_status', 'created_at')
# admin.site.register(JobApplication, JobApplicationAdmin)


admin.site.register(JobApplicationRemark)
admin.site.register(CandidateDiscussion)
admin.site.register(JobApplicationDocument)
admin.site.register(PreviousJobDetail)

