# Generated by Django 3.2.13 on 2022-05-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0016_auto_20220530_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d3category',
            name='categories',
            field=models.ManyToManyField(blank=True, to='charts.D3Category'),
        ),
    ]
