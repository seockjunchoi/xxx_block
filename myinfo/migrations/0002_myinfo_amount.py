# Generated by Django 2.1.4 on 2018-12-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
