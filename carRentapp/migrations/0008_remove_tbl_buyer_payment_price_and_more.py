# Generated by Django 4.0.4 on 2023-01-06 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carRentapp', '0007_tbl_review_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_buyer_payment',
            name='price',
        ),
        migrations.RemoveField(
            model_name='tbl_review',
            name='status',
        ),
    ]
