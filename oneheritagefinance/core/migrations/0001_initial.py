# Generated by Django 3.2.12 on 2022-04-30 12:06

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(choices=[('NGN', 'Nigerian Naira'), ('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound'), ('CNY', 'Chinese Yuan'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('DKK', 'Danish Krone'), ('SEK', 'Swedish Krona'), ('ZAR', 'South African Rand'), ('AED', 'United Arab Emirates Dirham')], default='USD', max_length=3, unique=True)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
                'ordering': ['code'],
            },
        ),
    ]