# Generated by Django 2.2.15 on 2020-10-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0009_ctf_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctf',
            name='flag',
            field=models.TextField(default='', max_length=100),
        ),
    ]