from rest_framework import serializers
from .models import JobApplication, JobApplicationRemark, CandidateDiscussion, JobApplicationDocument, PreviousJobDetail


class JobApplicationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, instance):
        created_at = instance.created_at.strftime("%Y-%m-%d")
        return created_at

    class Meta:
        model = JobApplication
        fields = '__all__'


class JobApplicationRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationRemark
        fields = '__all__'


class CandidateDiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDiscussion
        fields = '__all__'


class JobApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationDocument
        fields = '__all__'


class PreviousJobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousJobDetail
        fields = '__all__'
