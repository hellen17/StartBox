# Generated by Django 4.0.6 on 2022-09-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0019_remove_product_many_files_packages_packages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='file',
            new_name='guide',
        ),
        migrations.RenameField(
            model_name='packages',
            old_name='packages',
            new_name='product',
        ),
    ]
