# Generated by Django 4.2.11 on 2024-03-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_order_shippingaddress_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='', max_length=255, verbose_name='Name customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=255, verbose_name='Last name customer'),
        ),
    ]
