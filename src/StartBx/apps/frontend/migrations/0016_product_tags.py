# Generated by Django 4.0.6 on 2022-09-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_alter_product_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, choices=[('contracts', 'contracts'), ('agreement', 'agreement'), ('receipts', 'receipts')], default='', max_length=20),
        ),
    ]
