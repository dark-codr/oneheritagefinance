# Generated by Django 3.2.12 on 2022-04-30 22:01

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
# import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_account_acc_no'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('transfer_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw'), ('Debit', 'Debit')], default='Deposit', max_length=50)),
                ('purpose', models.TextField(verbose_name='Purpose for transaction')),
                ('status', models.CharField(choices=[('Verified', 'Verified'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Unverified', 'Unverified')], default='Unverified', max_length=15, verbose_name='Transaction Status')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_history', to='users.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transactional History',
                'verbose_name_plural': 'Transactional Histories',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('transfer_type', models.CharField(choices=[('Local', 'Local'), ('International', 'International')], default='Local', max_length=50, verbose_name='Transfer Type')),
                ('verified', models.CharField(choices=[('Verified', 'Verified'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Unverified', 'Unverified')], default='Unverified', max_length=15, verbose_name='Transaction Verified')),
                ('local_bank', models.CharField(blank=True, choices=[('', 'Select Bank'), ('Arvest Bank', 'Arvest Bank'), ('Ally Financial', 'Ally Financial'), ('American Express', 'American Express'), ('Amarillos National Bank', 'Amarillos National Bank'), ('Apple bank for Savings', 'Apple bank for Savings'), ('Bank of Hawaii', 'Bank of Hawaii'), ('Bank of Hope', 'Bank of Hope'), ('Bank United', 'Bank United'), ('BOA', 'Bank of America'), ('Bank United', 'Bank United'), ('Brown Brothers Harriman & Co', 'Brown Brothers Harriman & Co'), ('Barclays', 'Barclays'), ('BMO Harris Bank', 'BMO Harris Bank'), ('Bank OZK', 'Bank OZK'), ('BBVA Compass', 'BBVA Compass'), ('BNP Paribas', 'BNP Paribas'), ('BOK Financial Corporation', 'BOK Financial Corporation'), ('Cathay Bank', 'Cathay Bank'), ('Chartway Federal Credit Union', 'Chartway Federal Credit Union'), ('Capital One', 'Capital One'), ('Capital City Bank', 'Capital City Bank'), ('Chase Bank', 'Chase Bank'), ('Charles Schwab Corporation', 'Charles Schwab Corporation'), ('CG', 'CitiGroup'), ('Credit Suisse', 'Credit Suisse'), ('Comerica', 'Comerica'), ('CIT Group', 'CIT Group'), ('CapitalCity Bank', 'CapitalCity Bank'), ('Credit Union Page', 'Credit Union Page'), ('Citizens Federal Bank', 'Citizens Federal Bank'), ('Chemical Financial Corporation', 'Chemical Financial Corporation'), ('Discover Financial', 'Discover Financial'), ('Deutsche Bank', 'Deutsche Bank'), ('Douglas County Bank & Trust', 'Douglas County Bank & Trust '), ('Dime Savings Bank of Williamsburgh', 'Dime Savings Bank of Williamsburgh'), ('East West Bank', 'East West Bank'), ('Flagster Bank', 'Flagster Bank'), ('First National of Nebraska', 'First National of Nebraska'), ('FirstBank Holding Co', 'FirstBank Holding Co'), ('First Capital Bank', 'First Capital Bank'), ('First Commercial Bank', 'First Commercial Bank'), ('First Federal Savings Bank of Indiana', 'First Federal Savings Bank of Indiana'), ('First Guaranty Bank of Florida', 'First Guaranty Bank of Florida'), ('First Line Direct', 'First Line Direct'), ('First USA Bank', 'First USA Bank'), ('Fifth Third Bank', 'Fifth Third Bank'), ('First Citizens BancShares', 'First Citizens BancShares'), ('Fulton Financial Corporation', 'Fulton Financial Corporation'), ('First Hawaiian Bank', 'First Hawaiian Bank'), ('First Horizon National Corporation', 'First Horizon National Corporation'), ('Frost Bank', 'Frost Bank'), ('First Midwest Bank', 'First Midwest Bank'), ('Goldman Sachs', 'Goldman Sachs'), ('Grandeur Financial', 'Grandeur Financial'), ('HSBC Bank USA', 'HSBC Bank USA'), ('Home BancShares Conway', 'Home BancShares Conway'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Investors Bank', 'Investors Bank'), ('Íntercity State Bank', 'Íntercity State Bank'), ('KeyCorp', 'KeyCorp'), ('MB Financial', 'MB Financial'), ('Mizuho Financial Group', 'Mizuho Financial Group'), ('Midfirst Bank', 'Midfirst Bank'), ('M&T Bank', 'M&T Bank'), ('MUFG Union Bank ', 'MUFG Union Bank'), ('Morgan Stanley', 'Morgan Stanley'), ('Northern Trust', 'Northern Trust'), ('New  York Community Bank', 'New York Community Bank'), ('Old National Bank', 'Old National Bank'), ('Pacwest Bancorp', 'Pacwest Bancorp'), ('Pinnacle Financial Partners', 'Pinnacle Financial Partners'), ('PNC Financial Services', 'PNC Financial Services'), ('Raymond James Financial', 'Raymond James Financial'), ('RBC Bank', 'RBC Bank'), ('Region Financial Corporation', 'Region Financial Corporation'), ('Satander Bank', 'Satander Bank'), ('Synovus Columbus', 'Synovus Columbus'), ('Synchrony Financial', 'Synchrony Financial'), ('Sterling Bancorp', 'Sterling Bancorp'), ('Simmons Bank', 'Simmons Bank'), ('South State Bank', 'South State Bank'), ('Stifel St. Louise', 'Stifel St. Louise'), ('Suntrust Bank', 'Suntrust Bank'), ('TCF Financial Corporation', 'TCF Financial Corporation'), ('TD Bank', 'TD Bank'), ('The Bank of New York Mellon', 'The Bank of New York Mellon'), ('Texas Capital Bank', 'Texas Capital Bank'), ('UMB Financial Corporation', 'UMB Financial Corporation'), ('Utrecht-America', 'Utrecht-America'), ('United Bank', 'United Bank'), ('USAA', 'USAA'), ('U.S Bank', 'U.S Bank'), ('UBS', 'UBS'), ('Valley National Bank', 'Valley National Bank'), ('Washington Federal', 'Washington Federal'), ('Western Alliance Bancorporation', 'Western Alliance Bancorporation'), ('Wintrust Financial', 'Wintrust Financial'), ('Webster Bank', 'Webster Bank'), ('Wells Fargo', 'Wells Fargo'), ('Zions Bancorporation', 'Zions Bancorporation')], max_length=255, verbose_name='Local Banks')),
                ('acc_no', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999999999999)], verbose_name='NUBAN')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))], verbose_name='Transactional Amount')),
                ('purpose', models.TextField(verbose_name='Purpose for transaction')),
                ('recipients_bank', models.CharField(blank=True, max_length=500, verbose_name='Recipients Bank Name')),
                ('recipients_bank_swift', models.CharField(blank=True, max_length=50, verbose_name='Recipients Bank Swift Code')),
                ('recipients_name', models.CharField(blank=True, max_length=500, verbose_name='Recipients Account Name')),
                ('recipients_address', models.CharField(blank=True, max_length=500, verbose_name='Recipients Residential Address')),
                ('recipients_acc_no', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999999)], verbose_name='Recipients Account Number')),
                ('recipients_route_no', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(9999999999999)], verbose_name='Recipients Routing Number')),
                ('pin', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Transfer PIN')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Debit',
                'verbose_name_plural': 'Debits',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('acc_no', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(9999999999999999)])),
                ('pin', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Transfer PIN')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='depositor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Deposit',
                'verbose_name_plural': 'Deposits',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('acc_no', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(999999999999999999999)])),
                ('pin', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Transfer PIN')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='withdrawer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Withdrawal',
                'verbose_name_plural': 'Withdrawals',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]