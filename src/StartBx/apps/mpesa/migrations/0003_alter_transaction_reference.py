# Generated by Django 4.0.5 on 2022-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0002_alter_transaction_reference_alter_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(max_length=30),
        ),
    ]
