# Generated by Django 3.2.5 on 2021-07-31 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_detail', '0002_auto_20210731_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetail',
            old_name='products',
            new_name='product',
        ),
    ]
