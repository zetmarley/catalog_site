# Generated by Django 5.0.6 on 2024-05-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_version_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='название версии'),
        ),
    ]
