from rest_framework import serializers
from .models import Email, EmailTemplate
import re


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class EmailTemplateSerializer(serializers.ModelSerializer):
    variable_names = serializers.SerializerMethodField()

    class Meta:
        model = EmailTemplate
        fields = '__all__'

    def get_variable_names(self, obj):
        # Define the pattern to match Jinja variable names
        pattern = r'{{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*}}'

        # Find all matches in the template body
        matches = re.findall(pattern, obj.body)

        return matches
