# Generated by Django 4.0.5 on 2022-06-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_city_remove_order_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Success', max_length=30),
        ),
    ]