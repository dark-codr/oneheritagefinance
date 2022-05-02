# Generated by Django 3.2.12 on 2022-02-15 13:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.us.models
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'ordering': ['-date_joined'], 'verbose_name': 'User Account', 'verbose_name_plural': 'Users Account'},
        ),
        migrations.AddField(
            model_name='user',
            name='acc_no',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Checking Account', 'Checking Account'), ('Corporate Account', 'Corporate Account'), ('Savings Account', 'Savings Account')], default='Checking Account', max_length=18, verbose_name='Account Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='route_no',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)]),
        ),
        migrations.AddField(
            model_name='user',
            name='transaction_complete',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wallet Balance',
                'verbose_name_plural': 'Wallet Balances',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', stdimage.models.StdImageField(blank=True, upload_to='user/passport')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=14)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', localflavor.us.models.USPostalCodeField(max_length=2)),
                ('zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
                ('ssn', localflavor.us.models.USSocialSecurityNumberField(max_length=11)),
                ('country', models.ForeignKey(blank=True, default='US', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='countries_plus.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profile',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cookies_and_tracking', models.BooleanField(default=True, help_text='This is a must have integration to enable us provide you with proper services and security. They do not create any security bridge for you and can only be used to login, signout and even ensure your sessions are still working. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('google_ads', models.BooleanField(default=True, help_text='These is an advertising and devlivey network service, aimed solely to provide advert placements based on your browser informations. permiting this allows us provide you with adverts directly on our site. Be ensured that this does not constitute any security risk to you. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('social_account_integration', models.BooleanField(default=True, help_text='Facebook, Instagram, Twitter, Google Plus, Linkedin, these providers are integrated into the website to ensure we have proper informations to provide for our social influence and lead generation. We do not share these information for any other purpose other than statistical analysis. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('personal_information', models.BooleanField(default=True, help_text='These are personal informations we collect to provide quality and personalised services to you. They include (First Name, Last Name, Phone Number, Social Accounts, Addresses, Photo). You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('commercial_information', models.BooleanField(default=True, help_text='These are informations we collect for commercial purposes and are used for analysis as well as providing accurate data statistics of our services usage. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('identifiers', models.BooleanField(default=True, help_text='These are informations we collect to prevent fraud, do analysis as well as utilize cloud services. They include Email address, device identifiers (User IDs, IP and Location). You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('internet_or_other_electronic_network_activity_information', models.BooleanField(default=True, help_text='These are informations we collect regarding the user interactions within the website. With this information we can provide cloud services such as Content Delivery Networks for static/asset and media files. You hereby consent to the use and transfer of your Personal Information to countries outside the European Union.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprivacypolicy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Privacy',
                'verbose_name_plural': 'Users Privacy',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
    ]