# Generated by Django 2.1.4 on 2018-12-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0004_trade_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_info',
            name='gubun',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
