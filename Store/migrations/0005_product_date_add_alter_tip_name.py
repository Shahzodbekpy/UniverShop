# Generated by Django 4.1.7 on 2023-05-01 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_alter_tip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 1, 12, 46, 32, 941582)),
        ),
        migrations.AlterField(
            model_name='tip',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
