# Generated by Django 3.0.5 on 2020-04-02 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='cities')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='hourly_forecast_log',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hour', models.IntegerField()),
                ('desc', models.CharField(max_length=40)),
                ('temperature', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('wind_dir', models.IntegerField(null=True)),
                ('pressure', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
        migrations.CreateModel(
            name='daily_forecast_log',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('min_temperature', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('avg_humidity', models.FloatField()),
                ('sunrise_time', models.TimeField()),
                ('sunset_time', models.TimeField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.country'),
        ),
    ]
