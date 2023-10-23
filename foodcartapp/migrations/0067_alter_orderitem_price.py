# Generated by Django 3.2.15 on 2023-10-23 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0066_alter_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена в момент заказа'),
        ),
    ]
