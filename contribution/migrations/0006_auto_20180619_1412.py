# Generated by Django 2.0.6 on 2018-06-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0005_auto_20180619_0847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='data',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
