from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Company"

    def __str__(self):
        return self.name


class JobRole(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='job_role_documents/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Job role"

    def __str__(self):
        return self.title


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.city


class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Emergency Contact"

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    type = models.CharField(max_length=255, default="Document")

    class Meta:
        verbose_name_plural = "Documents"

    def __str__(self):
        return f"{self.name} - {self.type}"


class Achievement(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='Achievement_documents/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Achievements"

    def __str__(self):
        return self.title


class PerformanceReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='PerformanceReport_documents/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Performance Report"

    def __str__(self):
        return self.title



class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    profile_image = models.ImageField(upload_to="media/profile_image/", default='media/profile_image/default.png')
    DOB = models.DateField(null=True, blank=True)

    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    address = models.ManyToManyField(Address, blank=True)
    emergency_contacts = models.ManyToManyField(EmergencyContact, blank=True)
    documents = models.ManyToManyField(Document, blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)
    performance_reports = models.ManyToManyField(PerformanceReport, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    eligible_to_work = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email
