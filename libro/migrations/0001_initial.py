# Generated by Django 4.1.1 on 2022-09-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
