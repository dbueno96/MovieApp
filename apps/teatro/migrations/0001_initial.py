# Generated by Django 3.0.6 on 2020-05-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teatro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=15)),
            ],
        ),
    ]
