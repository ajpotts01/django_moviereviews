# Generated by Django 4.0 on 2023-01-01 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news posts'},
        ),
    ]
