# Generated by Django 4.0.6 on 2022-07-18 17:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_alter_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
