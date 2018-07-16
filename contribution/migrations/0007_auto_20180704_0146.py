# Generated by Django 2.0.6 on 2018-07-04 01:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0006_auto_20180619_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc'])], verbose_name='File: (Only pdf, docx or doc files with a maximum size of 2MB are allowed.)'),
        ),
    ]
