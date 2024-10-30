# Generated by Django 3.2.25 on 2024-10-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_student_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='departmental_email',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
