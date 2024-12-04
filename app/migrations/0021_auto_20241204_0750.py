# Generated by Django 3.2.25 on 2024-12-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_semester_is_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='instructor_remark',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='grade_remark',
            field=models.CharField(choices=[('passed', 'passed'), ('failed', 'failed'), ('pending', 'pending')], default='pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='grade_type',
            field=models.CharField(default='...', max_length=5, null=True),
        ),
    ]