# Generated by Django 4.0.5 on 2022-06-15 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
