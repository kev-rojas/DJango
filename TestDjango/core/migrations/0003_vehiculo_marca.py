# Generated by Django 3.2.3 on 2021-06-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_vehiculo_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(default=1, max_length=20, verbose_name='Marca'),
            preserve_default=False,
        ),
    ]
