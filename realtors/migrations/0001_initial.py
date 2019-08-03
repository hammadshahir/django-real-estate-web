# Generated by Django 2.2.2 on 2019-07-10 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtor_name', models.CharField(max_length=200)),
                ('realtor_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('realtor_description', models.TextField(blank=True)),
                ('realtor_email', models.EmailField(max_length=50)),
                ('realtor_phone', models.CharField(max_length=20)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hired_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
