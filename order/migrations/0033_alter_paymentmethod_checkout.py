# Generated by Django 4.2.7 on 2023-12-04 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0032_alter_paymentmethod_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='checkout',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='order.checkout'),
        ),
    ]
