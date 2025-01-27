# Generated by Django 4.0.4 on 2023-01-06 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carRentapp', '0010_delete_tbl_buyer_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_buyer_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(default='', max_length=250)),
                ('cardnum', models.CharField(default='', max_length=255)),
                ('expiry', models.CharField(default='', max_length=250)),
                ('cvvnum', models.CharField(default='', max_length=250)),
                ('status', models.CharField(default='', max_length=250)),
                ('price', models.CharField(default='', max_length=250)),
                ('buyer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carRentapp.tbl_user')),
                ('driver_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='carRentapp.tbl_user')),
            ],
        ),
    ]
