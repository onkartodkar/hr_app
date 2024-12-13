from django.contrib import admin
from .models import EmailTemplate, Email

admin.site.register(Email)


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version')
