# Generated by Django 5.1.1 on 2024-10-01 05:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='commentMessage_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('commentMsg', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('status', models.BooleanField(default=False)),
                ('createdDate', models.DateField(auto_now=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogerName', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=500)),
                ('mobileNo', models.CharField(default='', max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('age', models.IntegerField(null=True)),
                ('experience', models.IntegerField(default=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=500, null=True)),
                ('brief', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('mobile', models.CharField(default='', max_length=20)),
                ('admitDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
