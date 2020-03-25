# from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.db import models
# from django.urls import reverse
# from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager

# class User(AbstractUser):
class User(models.Model):
    username = models.CharField(
        # (max_length=30, unique=True, null=True, blank=True)

        ('username'), max_length=30, unique=True, null=True, blank=True,
        help_text=(
            'Required. 30 characters or fewer. Letters, digits and '
            '@/./+/-/_ only.'
        ),
        validators=[
            RegexValidator(
                '[\w\d.@+-]+$',
                ('Enter a valid username. '
                    'This value may contain only letters, numbers '
                    'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': ("A user with that username already exists."),
        })

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False, blank=False)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []



    # @property
    # def account_no(self):
    #     if hasattr(self, 'account'):
    #         return self.account.account_no
    #     return None

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return None

    @property
    def full_address(self):
        if hasattr(self, 'address'):
            return '{}, {}, {}'.format(
                self.address.street_address,
                self.address.city,
                # self.address.postal_code,
                self.address.country,
            )
        return None


class AccountDetails(models.Model):
    GENDER_CHOICE = (
        ("M", "Male"),
        ("F", "Female"),
    )
    PENSIONER_CHOICE = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    user = models.OneToOneField(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )
    account_no = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99999999)
        ]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    pensioner = models.CharField(max_length=3, choices=PENSIONER_CHOICE, verbose_name='Вы являетесь пенсионером?')


    def __str__(self):
        return str(self.user)


class UserAddress(models.Model):
    user = models.OneToOneField(
        User,
        related_name='address',
        on_delete=models.CASCADE,
    )
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    # postal_code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.user.email


class Passport(models.Model):
    user = models.OneToOneField(
        User,
        related_name='passport',
        on_delete=models.CASCADE,
    )
    series = models.CharField(max_length=3)
    number = models.IntegerField(unique=True, blank=True, null=True)
    issued_by = models.CharField(max_length=50)
    date_of_issue = models.DateField(null=True, blank=True)
    identification_number = models.IntegerField(unique=True, blank=True, null=True)
    # place_of_birth = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)

