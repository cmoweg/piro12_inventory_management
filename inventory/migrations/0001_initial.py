# Generated by Django 2.2.9 on 2020-01-26 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('seller_phone', models.CharField(max_length=13)),
                ('seller_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
                ('product_stock', models.IntegerField()),
                ('product_sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Seller')),
            ],
        ),
    ]
