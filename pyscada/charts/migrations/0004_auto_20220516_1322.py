# Generated by Django 2.2.28 on 2022-05-16 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_auto_20220516_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apexchart',
            name='library',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='libraryLinky', to='charts.ChartLibrarie'),
        ),
    ]
