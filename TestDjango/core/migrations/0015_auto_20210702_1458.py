# Generated by Django 3.2.3 on 2021-07-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_usuario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='imagen',
        ),
        migrations.AddField(
            model_name='obra',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Imagenes'),
        ),
    ]
