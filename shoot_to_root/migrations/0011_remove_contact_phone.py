# Generated by Django 2.2.20 on 2021-05-19 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0010_auto_20201009_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
