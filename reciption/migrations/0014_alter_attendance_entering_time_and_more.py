# Generated by Django 4.1.5 on 2023-03-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciption', '0013_alter_attendance_entering_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='entering_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='exit_time',
            field=models.TimeField(null=True),
        ),
    ]
