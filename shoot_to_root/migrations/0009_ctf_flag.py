# Generated by Django 2.2.15 on 2020-10-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0008_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctf',
            name='flag',
            field=models.TextField(default=''),
        ),
    ]
