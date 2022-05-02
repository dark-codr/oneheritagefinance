from decimal import Decimal

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    FileField,
    TextField,
    ForeignKey,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveBigIntegerField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    UUIDField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
# from tinymce import HTMLField

from oneheritagefinance.users.models import Account

User = settings.AUTH_USER_MODEL

BANKS = (
    ("", "Select Bank"),
    ("Arvest Bank", "Arvest Bank"),
    ("Ally Financial", "Ally Financial"),
    ("American Express", "American Express"),
    ("Amarillos National Bank", "Amarillos National Bank"),
    ("Apple bank for Savings", "Apple bank for Savings"),
    ("Bank of Hawaii", "Bank of Hawaii"),
    ("Bank of Hope", "Bank of Hope"),
    ("Bank United", "Bank United"),
    ("BOA", "Bank of America"),
    ("Bank United", "Bank United"),
    ("Brown Brothers Harriman & Co", "Brown Brothers Harriman & Co"),
    ("Barclays", "Barclays"),
    ("BMO Harris Bank", "BMO Harris Bank"),
    ("Bank OZK", "Bank OZK"),
    ("BBVA Compass", "BBVA Compass"),
    ("BNP Paribas", "BNP Paribas"),
    ("BOK Financial Corporation", "BOK Financial Corporation"),
    ("Cathay Bank", "Cathay Bank"),
    ("Chartway Federal Credit Union", "Chartway Federal Credit Union"),
    ("Capital One", "Capital One"),
    ("Capital City Bank", "Capital City Bank"),
    ("Chase Bank", "Chase Bank"),
    ("Charles Schwab Corporation", "Charles Schwab Corporation"),
    ("CG", "CitiGroup"),
    ("Credit Suisse", "Credit Suisse"),
    ("Comerica", "Comerica"),
    ("CIT Group", "CIT Group"),
    ("CapitalCity Bank", "CapitalCity Bank"),
    ("Credit Union Page", "Credit Union Page"),
    ("Citizens Federal Bank", "Citizens Federal Bank"),
    ("Chemical Financial Corporation", "Chemical Financial Corporation"),
    ("Discover Financial", "Discover Financial"),
    ("Deutsche Bank", "Deutsche Bank"),
    ("Douglas County Bank & Trust", "Douglas County Bank & Trust "),
    ("Dime Savings Bank of Williamsburgh", "Dime Savings Bank of Williamsburgh"),
    ("East West Bank", "East West Bank"),
    ("Flagster Bank", "Flagster Bank"),
    ("First National of Nebraska", "First National of Nebraska"),
    ("FirstBank Holding Co", "FirstBank Holding Co"),
    ("First Capital Bank", "First Capital Bank"),
    ("First Commercial Bank", "First Commercial Bank"),
    ("First Federal Savings Bank of Indiana", "First Federal Savings Bank of Indiana"),
    ("First Guaranty Bank of Florida", "First Guaranty Bank of Florida"),
    ("First Line Direct", "First Line Direct"),
    ("First USA Bank", "First USA Bank"),
    ("Fifth Third Bank", "Fifth Third Bank"),
    ("First Citizens BancShares", "First Citizens BancShares"),
    ("Fulton Financial Corporation", "Fulton Financial Corporation"),
    ("First Hawaiian Bank", "First Hawaiian Bank"),
    ("First Horizon National Corporation", "First Horizon National Corporation"),
    ("Frost Bank", "Frost Bank"),
    ("First Midwest Bank", "First Midwest Bank"),
    ("Goldman Sachs", "Goldman Sachs"),
    ("Grandeur Financial", "Grandeur Financial"),
    ("HSBC Bank USA", "HSBC Bank USA"),
    ("Home BancShares Conway", "Home BancShares Conway"),
    ("Huntington Bancshares", "Huntington Bancshares"),
    ("Investors Bank", "Investors Bank"),
    ("Íntercity State Bank", "Íntercity State Bank"),
    ("KeyCorp", "KeyCorp"),
    ("MB Financial", "MB Financial"),
    ("Mizuho Financial Group", "Mizuho Financial Group"),
    ("Midfirst Bank", "Midfirst Bank"),
    ("M&T Bank", "M&T Bank"),
    ("MUFG Union Bank ", "MUFG Union Bank"),
    ("Morgan Stanley", "Morgan Stanley"),
    ("Northern Trust", "Northern Trust"),
    ("New  York Community Bank", "New York Community Bank"),
    ("Old National Bank", "Old National Bank"),
    ("Pacwest Bancorp", "Pacwest Bancorp"),
    ("Pinnacle Financial Partners", "Pinnacle Financial Partners"),
    ("PNC Financial Services", "PNC Financial Services"),
    ("Raymond James Financial", "Raymond James Financial"),
    ("RBC Bank", "RBC Bank"),
    ("Region Financial Corporation", "Region Financial Corporation"),
    ("Satander Bank", "Satander Bank"),
    ("Synovus Columbus", "Synovus Columbus"),
    ("Synchrony Financial", "Synchrony Financial"),
    ("Sterling Bancorp", "Sterling Bancorp"),
    ("Simmons Bank", "Simmons Bank"),
    ("South State Bank", "South State Bank"),
    ("Stifel St. Louise", "Stifel St. Louise"),
    ("Suntrust Bank", "Suntrust Bank"),
    ("TCF Financial Corporation", "TCF Financial Corporation"),
    ("TD Bank", "TD Bank"),
    ("The Bank of New York Mellon", "The Bank of New York Mellon"),
    ("Texas Capital Bank", "Texas Capital Bank"),
    ("UMB Financial Corporation", "UMB Financial Corporation"),
    ("Utrecht-America", "Utrecht-America"),
    ("United Bank", "United Bank"),
    ("USAA", "USAA"),
    ("U.S Bank", "U.S Bank"),
    ("UBS", "UBS"),
    ("Valley National Bank", "Valley National Bank"),
    ("Washington Federal", "Washington Federal"),
    ("Western Alliance Bancorporation", "Western Alliance Bancorporation"),
    ("Wintrust Financial", "Wintrust Financial"),
    ("Webster Bank", "Webster Bank"),
    ("Wells Fargo", "Wells Fargo"),
    ("Zions Bancorporation", "Zions Bancorporation"),
)

SELECT_BANK = [
    "Arvest Bank",
    "Ally Financial",
    "American Express",
    "Amarillos National Bank",
    "Apple bank for Savings",
    "Bank of Hawaii",
    "Bank of Hope",
    "Bank United",
    "BOA",
    "Bank United",
    "Brown Brothers Harriman & Co",
    "Barclays",
    "BMO Harris Bank",
    "Bank OZK",
    "BBVA Compass",
    "BNP Paribas",
    "BOK Financial Corporation",
    "Cathay Bank",
    "Chartway Federal Credit Union",
    "Capital One",
    "Capital City Bank",
    "Chase Bank",
    "Charles Schwab Corporation",
    "CG",
    "Credit Suisse",
    "Comerica",
    "CIT Group",
    "CapitalCity Bank",
    "Credit Union Page",
    "Citizens Federal Bank",
    "Chemical Financial Corporation",
    "Discover Financial",
    "Deutsche Bank",
    "Douglas County Bank & Trust",
    "Dime Savings Bank of Williamsburgh",
    "East West Bank",
    "Flagster Bank",
    "First National of Nebraska",
    "FirstBank Holding Co",
    "First Capital Bank",
    "First Commercial Bank",
    "First Federal Savings Bank of Indiana",
    "First Guaranty Bank of Florida",
    "First Line Direct",
    "First USA Bank",
    "Fifth Third Bank",
    "First Citizens BancShares",
    "Fulton Financial Corporation",
    "First Hawaiian Bank",
    "First Horizon National Corporation",
    "Frost Bank",
    "First Midwest Bank",
    "Goldman Sachs",
    "Grandeur Financial",
    "HSBC Bank USA",
    "Home BancShares Conway",
    "Huntington Bancshares",
    "Investors Bank",
    "Íntercity State Bank",
    "KeyCorp",
    "MB Financial",
    "Mizuho Financial Group",
    "Midfirst Bank",
    "M&T Bank",
    "MUFG Union Bank ",
    "Morgan Stanley",
    "Northern Trust",
    "New  York Community Bank",
    "Old National Bank",
    "Pacwest Bancorp",
    "Pinnacle Financial Partners",
    "PNC Financial Services",
    "Raymond James Financial",
    "RBC Bank",
    "Region Financial Corporation",
    "Satander Bank",
    "Synovus Columbus",
    "Synchrony Financial",
    "Sterling Bancorp",
    "Simmons Bank",
    "South State Bank",
    "Stifel St. Louise",
    "Suntrust Bank",
    "TCF Financial Corporation",
    "TD Bank",
    "The Bank of New York Mellon",
    "Texas Capital Bank",
    "UMB Financial Corporation",
    "Utrecht-America",
    "United Bank",
    "USAA",
    "U.S Bank",
    "UBS",
    "Valley National Bank",
    "Washington Federal",
    "Western Alliance Bancorporation",
    "Wintrust Financial",
    "Webster Bank",
    "Wells Fargo",
    "Zions Bancorporation",
]


class Deposit(TimeStampedModel):
    UNVERIFIED = "Unverified"
    VERIFIED = "Verified"
    PENDING = "Pending"
    BLOCKED = "Blocked"
    VERIFICATION_STATUS = (
        (VERIFIED, VERIFIED),
        (PENDING, PENDING),
        (BLOCKED, BLOCKED),
        (UNVERIFIED, UNVERIFIED),
    )

    verified = CharField(
        _("Transaction Verified"),
        max_length=15,
        choices=VERIFICATION_STATUS,
        default=UNVERIFIED,
    )
    user = ForeignKey(User, related_name="depositor", on_delete=DO_NOTHING)
    amount = DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("10.00"))],
    )
    acc_no = PositiveIntegerField(
        blank=False,
        null=True,
        validators=[MinValueValidator(1000000), MaxValueValidator(9999999999999999)],
    )

    pin = PositiveIntegerField(
        _("Transfer PIN"),
        blank=True,
        null=True,
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )

    def __str__(self):
        return f"{self.user.name.title()} Deposits"

    class Meta:
        verbose_name = _("Deposit")
        verbose_name_plural = _("Deposits")
        ordering = ["-created"]


class Withdraw(TimeStampedModel):
    UNVERIFIED = "Unverified"
    VERIFIED = "Verified"
    PENDING = "Pending"
    BLOCKED = "Blocked"
    VERIFICATION_STATUS = (
        (VERIFIED, VERIFIED),
        (PENDING, PENDING),
        (BLOCKED, BLOCKED),
        (UNVERIFIED, UNVERIFIED),
    )

    verified = CharField(
        _("Transaction Verified"),
        max_length=15,
        choices=VERIFICATION_STATUS,
        default=UNVERIFIED,
    )
    user = ForeignKey(User, related_name="withdrawer", on_delete=DO_NOTHING)
    amount = DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("10.00"))],
    )
    acc_no = PositiveBigIntegerField(
        blank=False,
        null=True,
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(999999999999999999999),
        ],
    )

    pin = PositiveIntegerField(
        _("Transfer PIN"),
        blank=True,
        null=True,
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )

    def __str__(self):
        return f"{self.user.name.title()} Withdrawals"

    class Meta:
        verbose_name = _("Withdrawal")
        verbose_name_plural = _("Withdrawals")
        ordering = ["-created"]


class Debit(TimeStampedModel):
    LOCAL = "Local"
    INTERNATIONAL = "International"
    TRANS_TYPE = ((LOCAL, LOCAL), (INTERNATIONAL, INTERNATIONAL))
    UNVERIFIED = "Unverified"
    VERIFIED = "Verified"
    PENDING = "Pending"
    BLOCKED = "Blocked"
    VERIFICATION_STATUS = (
        (VERIFIED, VERIFIED),
        (PENDING, PENDING),
        (BLOCKED, BLOCKED),
        (UNVERIFIED, UNVERIFIED),
    )

    transfer_type = CharField(
        _("Transfer Type"), max_length=50, choices=TRANS_TYPE, default=LOCAL
    )
    verified = CharField(
        _("Transaction Verified"),
        max_length=15,
        choices=VERIFICATION_STATUS,
        default=UNVERIFIED,
    )

    local_bank = CharField(_("Local Banks"), blank=True, max_length=255, choices=BANKS)

    user = ForeignKey(User, related_name="user", on_delete=DO_NOTHING)
    acc_no = PositiveBigIntegerField(
        _("NUBAN"),
        blank=False,
        null=True,
        validators=[MinValueValidator(10000000), MaxValueValidator(99999999999999999)],
    )
    amount = DecimalField(
        _("Transactional Amount"),
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("10.00"))],
    )

    purpose = TextField(_("Purpose for transaction"))

    recipients_bank = CharField(_("Recipients Bank Name"), max_length=500, blank=True)
    recipients_bank_swift = CharField(
        _("Recipients Bank Swift Code"), max_length=50, blank=True
    )
    recipients_name = CharField(
        _("Recipients Account Name"), max_length=500, blank=True
    )
    recipients_address = CharField(
        _("Recipients Residential Address"), max_length=500, blank=True
    )
    recipients_acc_no = PositiveBigIntegerField(
        _("Recipients Account Number"),
        blank=True,
        null=True,
        validators=[MinValueValidator(100000), MaxValueValidator(99999999999999999999)],
    )
    recipients_route_no = PositiveBigIntegerField(
        _("Recipients Routing Number"),
        blank=True,
        null=True,
        validators=[MinValueValidator(100000), MaxValueValidator(99999999999999999999)],
    )

    pin = PositiveIntegerField(
        _("Transfer PIN"),
        blank=True,
        null=True,
        unique=False,
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )

    def __str__(self):
        return f"{self.user.name.title()} Debits"

    class Meta:
        verbose_name = _("Debit")
        verbose_name_plural = _("Debits")
        ordering = ["-created"]


class AccountHistory(TimeStampedModel):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    TRANSFER = "Debit"
    TRANS_TYPE = ((DEPOSIT, DEPOSIT), (WITHDRAW, WITHDRAW), (TRANSFER, TRANSFER))

    UNVERIFIED = "Unverified"
    VERIFIED = "Verified"
    PENDING = "Pending"
    BLOCKED = "Blocked"
    VERIFICATION_STATUS = (
        (VERIFIED, VERIFIED),
        (PENDING, PENDING),
        (BLOCKED, BLOCKED),
        (UNVERIFIED, UNVERIFIED),
    )
    user = ForeignKey(User, related_name="history", on_delete=DO_NOTHING)
    transfer_type = CharField(max_length=50, choices=TRANS_TYPE, default=DEPOSIT)
    purpose = TextField(_("Purpose for transaction"))
    status = CharField(
        _("Transaction Status"),
        max_length=15,
        choices=VERIFICATION_STATUS,
        default=UNVERIFIED,
    )
    account = ForeignKey(Account, on_delete=DO_NOTHING, related_name="account_history")
    amount = DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("10.00"))],
    )

    def __str__(self):
        return f"{self.account.user.name.title()} Account History"

    class Meta:
        verbose_name = _("Transactional History")
        verbose_name_plural = _("Transactional Histories")
        ordering = ["-created"]
