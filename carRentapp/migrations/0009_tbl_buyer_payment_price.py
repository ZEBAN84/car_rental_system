# Generated by Django 4.0.4 on 2023-01-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentapp', '0008_remove_tbl_buyer_payment_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_buyer_payment',
            name='price',
            field=models.CharField(default='', max_length=250),
        ),
    ]
