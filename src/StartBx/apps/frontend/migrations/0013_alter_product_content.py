# Generated by Django 4.0.4 on 2022-05-25 18:32

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_packages_remove_product_url_product_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(null=True),
        ),
    ]
