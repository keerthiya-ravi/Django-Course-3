# Generated by Django 3.1.3 on 2020-11-03 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bgimg',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 16, 20, 21, 522829)),
        ),
    ]
