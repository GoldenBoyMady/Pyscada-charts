# Generated by Django 3.2.13 on 2022-05-19 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0097_auto_20220118_1046'),
        ('charts', '0004_auto_20220516_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartD3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=400)),
                ('variables', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='D3variables', to='pyscada.variable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriesD3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=400)),
                ('link_type', models.BooleanField(default=False, help_text='Link')),
                ('links', models.PositiveSmallIntegerField(choices=[(0, 'Variable'), (1, 'Category')], default=2, help_text='Linked variables or categories')),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.chartd3')),
            ],
        ),
    ]
