# Generated by Django 2.2.15 on 2020-10-06 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0006_auto_20201005_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('index', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
