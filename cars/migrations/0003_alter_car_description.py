# Generated by Django 4.1.2 on 2022-10-19 01:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20221019_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
