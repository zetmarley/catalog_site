# Generated by Django 4.2.2 on 2024-06-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='публикация'),
        ),
    ]