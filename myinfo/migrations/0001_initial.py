# Generated by Django 2.1.4 on 2018-12-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myinfo',
            fields=[
                ('inx', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=20)),
                ('name_reg', models.CharField(blank=True, max_length=50, null=True)),
                ('jumin_number', models.CharField(blank=True, max_length=50, null=True)),
                ('sex_reg', models.CharField(blank=True, max_length=10, null=True)),
                ('email_reg', models.CharField(blank=True, max_length=100, null=True)),
                ('marry_reg', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
