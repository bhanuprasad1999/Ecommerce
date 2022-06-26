# Generated by Django 4.0.5 on 2022-06-26 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('quantity_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_uom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.FloatField()),
                ('product_price', models.PositiveIntegerField()),
                ('product_quantity_uom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.productquantity')),
                ('product_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.products')),
            ],
        ),
    ]