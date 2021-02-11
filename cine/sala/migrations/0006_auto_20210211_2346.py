# Generated by Django 3.1.6 on 2021-02-11 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0005_auto_20210211_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación en db'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sala',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de última actualización en db'),
        ),
    ]
