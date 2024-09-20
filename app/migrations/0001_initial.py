# Generated by Django 3.2.25 on 2024-09-18 10:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.college')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('courseCode', models.CharField(blank=True, max_length=15, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.level')),
                ('programmes', models.ManyToManyField(related_name='courses', to='app.Programme')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('otherNames', models.CharField(blank=True, max_length=80, null=True)),
                ('surname', models.CharField(blank=True, max_length=80, null=True)),
                ('level', models.CharField(blank=True, max_length=80, null=True)),
                ('matricNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('studentPhoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField(blank=True, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('courses', models.ManyToManyField(to='app.Course')),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instructor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]