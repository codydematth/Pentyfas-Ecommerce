# Generated by Django 3.2.9 on 2021-12-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
