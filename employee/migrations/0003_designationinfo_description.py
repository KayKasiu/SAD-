# Generated by Django 4.1.5 on 2023-01-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employeeinfo_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='designationinfo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]