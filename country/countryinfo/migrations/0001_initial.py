# Generated by Django 4.2.7 on 2024-01-16 08:41

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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('population', models.IntegerField()),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='continent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('population', models.IntegerField()),
                ('size', models.IntegerField()),
                ('biggestcountry', models.CharField(max_length=30)),
                ('smallestcountry', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('GDP', models.IntegerField()),
                ('age_made', models.IntegerField()),
                ('capital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countryinfo.city')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countryinfo.continent')),
            ],
        ),
    ]
