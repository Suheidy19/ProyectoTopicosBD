# Generated by Django 3.2.7 on 2021-10-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Descripción'),
        ),
    ]
