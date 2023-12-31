# Generated by Django 4.2.6 on 2023-11-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rename_zip_checkout_zip_code_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('upi', 'UPI ID')], max_length=50),
        ),
    ]
