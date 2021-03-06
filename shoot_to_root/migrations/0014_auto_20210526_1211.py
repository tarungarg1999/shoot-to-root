# Generated by Django 2.2.20 on 2021-05-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoot_to_root', '0013_auto_20210521_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(default='', max_length=50)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='ctf',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
