# Generated by Django 5.0 on 2024-01-04 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notification_application'),
        ('onboarding', '0005_candidatediscussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='application',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='onboarding.jobapplication'),
        ),
    ]
