# Generated by Django 3.0.6 on 2020-06-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0004_auto_20200601_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(default='pelicula/default.png', upload_to='pelicula/'),
        ),
    ]
