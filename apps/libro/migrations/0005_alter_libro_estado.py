# Generated by Django 4.1.3 on 2022-11-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libro", "0004_libro_estado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="libro",
            name="estado",
            field=models.BooleanField(default=True, verbose_name="Estado"),
        ),
    ]
