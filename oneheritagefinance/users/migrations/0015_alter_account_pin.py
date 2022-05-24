# Generated by Django 3.2.12 on 2022-05-24 21:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20220524_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1111), django.core.validators.MaxValueValidator(9999)], verbose_name='Transfer PIN'),
        ),
    ]
