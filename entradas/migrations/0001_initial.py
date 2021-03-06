# Generated by Django 4.0.4 on 2022-06-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('contenido', models.TextField(default='DEFAULT VALUE')),
                ('imagen', models.FileField(upload_to='')),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('actualizado_el', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'entradas',
            },
        ),
    ]
