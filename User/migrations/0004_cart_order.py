# Generated by Django 2.1 on 2023-11-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20231101_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=32)),
                ('number', models.IntegerField()),
                ('item', models.CharField(default='', max_length=32)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField()),
                ('buyers', models.CharField(default='', max_length=32)),
                ('number', models.IntegerField()),
                ('item', models.CharField(default='', max_length=32)),
                ('price', models.FloatField()),
            ],
        ),
    ]