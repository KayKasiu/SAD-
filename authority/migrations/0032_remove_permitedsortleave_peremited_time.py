# Generated by Django 4.1.5 on 2023-03-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0031_permitedsortleave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permitedsortleave',
            name='peremited_time',
        ),
    ]