# Generated by Django 3.0.4 on 2020-03-23 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='pensioner',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Вы являетесь пенсионером?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator('[\\w\\d.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username'),
        ),
    ]
