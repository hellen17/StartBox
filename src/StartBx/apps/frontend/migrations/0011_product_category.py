# Generated by Django 4.0.4 on 2022-04-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_remove_product_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Package', 'Package'), ('Template', 'Template')], default=5, max_length=20),
            preserve_default=False,
        ),
    ]
