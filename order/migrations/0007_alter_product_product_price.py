# Generated by Django 4.2.6 on 2023-11-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]