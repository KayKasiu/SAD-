# Generated by Django 4.1.5 on 2023-02-05 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SetOfficeTime',
            new_name='OfficeTime',
        ),
    ]
