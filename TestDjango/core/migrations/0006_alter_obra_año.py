# Generated by Django 3.2.3 on 2021-06-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_obra_tamaño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='año',
            field=models.CharField(max_length=20, verbose_name='Año'),
        ),
    ]
