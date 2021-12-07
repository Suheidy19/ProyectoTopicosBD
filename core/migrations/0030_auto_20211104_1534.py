# Generated by Django 3.2.7 on 2021-11-04 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_firstname_client_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cite',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='mascot',
            old_name='foto',
            new_name='Foto',
        ),
        migrations.RenameField(
            model_name='mascot',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='mascot',
            old_name='race',
            new_name='Race',
        ),
        migrations.RenameField(
            model_name='mascot',
            old_name='type',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='Quantity',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='firstname',
            new_name='Firstname',
        ),
    ]
