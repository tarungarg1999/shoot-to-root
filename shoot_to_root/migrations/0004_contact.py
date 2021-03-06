# Generated by Django 2.2.15 on 2020-10-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0003_auto_20201004_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('comment', models.TextField(max_length=5000)),
            ],
        ),
    ]
