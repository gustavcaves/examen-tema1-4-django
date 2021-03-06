# Generated by Django 3.1.6 on 2021-02-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0003_auto_20210211_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la sala')),
                ('number_chair', models.IntegerField(max_length=1500, verbose_name='Número de Sillas')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ['name', 'number_chair'],
            },
        ),
    ]
