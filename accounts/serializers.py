from rest_framework import serializers
from .models import Company, JobRole, Address, EmergencyContact, Document, Achievement, PerformanceReport, User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class PerformanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReport
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    emergency_contacts = EmergencyContactSerializer(many=True)
    documents = DocumentSerializer(many=True)
    achievements = AchievementSerializer(many=True)
    performance_reports = PerformanceReportSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
