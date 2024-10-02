# Generated by Django 3.2.25 on 2024-09-23 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20240923_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=9)),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='year',
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_date', models.DateField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='session',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.session'),
        ),
        migrations.AddField(
            model_name='student',
            name='sessions',
            field=models.ManyToManyField(default=None, null=True, through='app.Enrollment', to='app.Session'),
        ),
    ]