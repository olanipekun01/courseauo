# Generated by Django 3.2.25 on 2024-09-23 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='session',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='date_approved',
        ),
        migrations.AddField(
            model_name='registration',
            name='carried_over',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
        migrations.AddField(
            model_name='registration',
            name='passed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
