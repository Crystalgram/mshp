# Generated by Django 3.1.2 on 2020-10-20 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='item_name',
            new_name='item_title',
        ),
    ]
