# Generated by Django 3.2.13 on 2022-05-20 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0097_auto_20220118_1046'),
        ('charts', '0007_rename_chartd3_d3chart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoriesD3',
            new_name='D3Category',
        ),
    ]
