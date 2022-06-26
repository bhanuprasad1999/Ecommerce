# Generated by Django 4.0.5 on 2022-06-26 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_order_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_stock_status',
            field=models.CharField(choices=[('outstock', 'Out of Stock'), ('instock', 'Stock Avaliable'), ('coming', 'Coming soon')], default='instock', max_length=100),
        ),
    ]