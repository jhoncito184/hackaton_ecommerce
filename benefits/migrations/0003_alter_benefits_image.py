# Generated by Django 3.2.5 on 2021-07-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0002_benefits_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefits',
            name='image',
            field=models.TextField(),
        ),
    ]
