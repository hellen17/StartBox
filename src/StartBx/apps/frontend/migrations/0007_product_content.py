# Generated by Django 4.0.3 on 2022-03-31 20:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_product_id_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
