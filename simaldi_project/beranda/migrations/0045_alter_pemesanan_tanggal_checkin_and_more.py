# Generated by Django 4.2.1 on 2023-08-13 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0044_alter_pemesanan_foto_ktp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 18, 22, 40, 686354, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkout',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 18, 22, 40, 686354, tzinfo=datetime.timezone.utc)),
        ),
    ]
