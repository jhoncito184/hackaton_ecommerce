# Generated by Django 3.2.5 on 2021-08-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.TextField(null=True),
        ),
    ]
