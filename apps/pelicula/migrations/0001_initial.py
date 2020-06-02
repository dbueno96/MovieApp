# Generated by Django 3.0.6 on 2020-05-19 03:02

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('duracion', models.TimeField(default=datetime.time(0, 0))),
                ('genero', models.CharField(choices=[('dr', 'Drama'), ('com', 'Comedia'), ('ter', 'Terror'), ('th', 'Thriller'), ('inf', 'Infantil')], max_length=5)),
                ('pais', django_countries.fields.CountryField(max_length=15)),
            ],
        ),
    ]