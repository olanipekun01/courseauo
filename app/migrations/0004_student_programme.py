# Generated by Django 3.2.25 on 2024-09-18 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='programme',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.programme'),
        ),
    ]