# Generated by Django 3.2.12 on 2022-04-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_account_acc_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_no',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Account Number'),
        ),
    ]
