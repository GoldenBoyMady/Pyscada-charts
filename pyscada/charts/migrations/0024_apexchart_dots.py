# Generated by Django 3.2.13 on 2022-06-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0023_auto_20220614_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='apexchart',
            name='dots',
            field=models.BooleanField(default=False, help_text='Enable dots on lines'),
        ),
    ]
