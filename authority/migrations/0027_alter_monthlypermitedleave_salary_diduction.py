# Generated by Django 4.1.5 on 2023-03-01 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0026_monthlypermitedleave_salary_diduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlypermitedleave',
            name='salary_diduction',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
