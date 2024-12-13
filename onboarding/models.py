from django.db import models
from accounts.models import JobRole, User

APPLICATION_STATUS = (
    ('Pending Approval', 'Pending Approval'),
    ('Approved', 'Approved'),
    ('In Progress', 'In Progress'),
    ('Update', 'Update'),

    ('On hold', 'On hold'),
    ('Rejected', 'Rejected'),
    ('Blocked', 'Blocked'),

    ('Onboard', 'Onboard'),
)

APPLICATION_STATUS_DEFAULT = 'Pending Approval'

DOCUMENT_STATUS = (
    ('Pending Review', 'Pending Review'),
    ('Reviewed', 'Reviewed'),
    ('In Progress', 'In Progress'),
    ('Update', 'Update'),
    ('On hold', 'On hold'),
    ('Rejected', 'Rejected'),
    ('Blocked', 'Blocked'),
    ('Approved', 'Approved'),
)

DOCUMENT_STATUS_DEFAULT = 'Pending Review'


class JobApplication(models.Model):
    applicant_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    resume = models.FileField(upload_to='job_applications/resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_job = models.ForeignKey(JobRole, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default=APPLICATION_STATUS_DEFAULT)
    tech_interview_clear = models.BooleanField(default=False)
    hr_interview_clear = models.BooleanField(default=False)
    payment_terms_agreed = models.BooleanField(default=False)
    offer_letter_accepted = models.BooleanField(default=False)
    joining_letter_recieved = models.BooleanField(default=False)
    documents_verified = models.BooleanField(default=False)
    documentation_status = models.CharField(max_length=20, choices=DOCUMENT_STATUS, default=DOCUMENT_STATUS_DEFAULT)

    class Meta:
        verbose_name_plural = "Job Application"

    def __str__(self):
        return self.applicant_name


class JobApplicationRemark(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='remarks')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Candidate Application Remark"

    def __str__(self):
        return self.application.applicant_name


class CandidateDiscussion(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='discussion')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Candidate Discussion"

    def __str__(self):
        return self.application


class JobApplicationDocument(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, default="Document")
    file = models.FileField(upload_to='job_application_documents/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Candidate Documents"

    def __str__(self):
        return f"{self.application} - {self.type}"


class PreviousJobDetail(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='previous_jobs')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Candidate Previous Job Details"

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
