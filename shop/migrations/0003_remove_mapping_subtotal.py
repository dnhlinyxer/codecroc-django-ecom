# Generated by Django 3.2.8 on 2021-10-14 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapping',
            name='subtotal',
        ),
    ]
