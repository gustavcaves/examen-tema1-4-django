# Generated by Django 3.1.6 on 2021-02-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0002_auto_20210211_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programacionsala',
            options={'ordering': ['datee', 'movie'], 'verbose_name': 'Programacion de Película', 'verbose_name_plural': 'Programación de Películas'},
        ),
        migrations.RenameField(
            model_name='programacionsala',
            old_name='date',
            new_name='datee',
        ),
    ]
