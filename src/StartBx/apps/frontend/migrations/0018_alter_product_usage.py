# Generated by Django 4.0.6 on 2022-09-19 12:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0017_product_usage_product_who_needs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='usage',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]