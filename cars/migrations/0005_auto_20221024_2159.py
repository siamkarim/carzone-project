# Generated by Django 3.0.7 on 2022-10-24 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_title',
            new_name='car_title',
        ),
    ]