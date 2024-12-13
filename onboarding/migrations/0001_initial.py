# Generated by Django 4.2 on 2023-12-26 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('resume', models.FileField(blank=True, null=True, upload_to='job_applications/resumes/')),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application_status', models.CharField(default='pending_approval', max_length=20)),
                ('tech_interview_clear', models.BooleanField(default=False)),
                ('hr_interview_clear', models.BooleanField(default=False)),
                ('payment_terms_agreed', models.BooleanField(default=False)),
                ('offer_letter_accepted', models.BooleanField(default=False)),
                ('joining_letter_recieved', models.BooleanField(default=False)),
                ('documents_verified', models.BooleanField(default=False)),
                ('documentation_status', models.CharField(default='pending', max_length=20)),
                ('applied_job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.jobrole')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousJobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_jobs', to='onboarding.jobapplication')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicationRemark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remarks', to='onboarding.jobapplication')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicationDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Document', max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='job_application_documents/')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onboarding.jobapplication')),
            ],
        ),
    ]
