# Generated by Django 4.1 on 2024-10-15 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20241014_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='level',
            new_name='currentlevel',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sessions',
            new_name='entrySessions',
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.college'),
        ),
        migrations.AddField(
            model_name='student',
            name='currentSession',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='entryLevel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='localGovtArea',
            field=models.CharField(blank=True, max_length=110, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='modeOfEntry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=110, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='stateOfOrigin',
            field=models.CharField(blank=True, max_length=110, null=True),
        ),
    ]
