# Generated by Django 3.2.12 on 2022-05-02 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_account_acc_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_no',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(234000000), django.core.validators.MaxValueValidator(99999999999999999)], verbose_name='Account Number'),
        ),
    ]
