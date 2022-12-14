# Generated by Django 4.1.2 on 2022-10-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebScrapData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('h1', models.CharField(max_length=100)),
                ('h24', models.CharField(max_length=100)),
                ('d7', models.CharField(max_length=100)),
                ('market_cap', models.CharField(max_length=100)),
                ('volume_24h', models.CharField(max_length=100)),
                ('circulating_supply', models.CharField(max_length=100)),
            ],
        ),
    ]
