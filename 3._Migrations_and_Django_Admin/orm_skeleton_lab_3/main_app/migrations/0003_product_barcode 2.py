# Generated by Django 4.2.4 on 2023-10-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_product_created_on_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
