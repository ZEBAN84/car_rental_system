# Generated by Django 4.0.4 on 2023-01-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentapp', '0005_tbl_buyer_payment_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_buyer_car_payment',
            name='price',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='tbl_buyer_payment',
            name='price',
            field=models.CharField(default='', max_length=250),
        ),
    ]
