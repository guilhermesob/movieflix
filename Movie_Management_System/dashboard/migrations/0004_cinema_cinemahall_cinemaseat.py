# Generated by Django 3.1.7 on 2021-03-25 20:48

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_cinema_halls', models.IntegerField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.city')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_seats', models.IntegerField()),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('type', django_mysql.models.EnumField(choices=[('Basic', 'Basic'), ('Executive', 'Executive'), ('Premium', 'Premium'), ('VIP', 'VIP')])),
                ('cinemal_hall_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cinemahall')),
            ],
        ),
    ]
