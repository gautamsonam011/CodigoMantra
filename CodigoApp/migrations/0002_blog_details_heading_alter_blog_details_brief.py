# Generated by Django 5.1.1 on 2024-10-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodigoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_details',
            name='heading',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog_details',
            name='brief',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
