# Generated by Django 3.1.7 on 2021-05-24 15:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dukan', '0005_auto_20210524_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='saman',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='saman',
            name='mfd',
            field=models.TimeField(default=datetime.datetime(2021, 5, 24, 15, 3, 13, 249700, tzinfo=utc)),
        ),
    ]
