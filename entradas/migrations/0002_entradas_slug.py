# Generated by Django 4.0.4 on 2022-06-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradas',
            name='slug',
            field=models.CharField(default='DEFAUL VALUE', max_length=5000),
        ),
    ]
