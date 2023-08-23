# Generated by Django 4.2.1 on 2023-07-11 01:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0038_alter_pemesanan_tanggal_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.datetime(2023, 7, 11, 1, 5, 27, 904718, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkout',
            field=models.DateField(default=datetime.datetime(2023, 7, 11, 1, 5, 27, 904718, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Notifikasipembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesan', models.CharField(max_length=255)),
                ('dibaca', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pembayaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beranda.pembayaran')),
            ],
        ),
    ]
