# Generated by Django 5.1.6 on 2025-02-25 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jorgeluisapp', '0009_alter_meteoritelanding_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='fall',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='geolocation',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='mass',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='meteorite_id',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='nametype',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='recclass',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='reclat',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='reclong',
        ),
        migrations.RemoveField(
            model_name='meteoritelanding',
            name='year',
        ),
    ]
