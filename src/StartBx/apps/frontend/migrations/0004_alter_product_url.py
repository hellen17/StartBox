# Generated by Django 4.0.3 on 2022-03-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_remove_product_zipped_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
