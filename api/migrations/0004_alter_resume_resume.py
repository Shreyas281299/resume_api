# Generated by Django 3.2 on 2021-06-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210613_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(upload_to='Users/apple/Desktop/Internship/resume_api/Resume'),
        ),
    ]
