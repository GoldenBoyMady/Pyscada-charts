# Generated by Django 3.2.13 on 2022-06-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0021_auto_20220602_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='apexchart',
            name='stacked',
            field=models.BooleanField(default=False, help_text='Display stacked data'),
        ),
    ]
