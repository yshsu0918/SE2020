# Generated by Django 3.0.7 on 2020-06-28 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BAG', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_record',
            old_name='buy_id',
            new_name='item_id',
        ),
    ]
