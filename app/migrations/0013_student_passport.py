# Generated by Django 3.2.25 on 2024-10-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_student_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
