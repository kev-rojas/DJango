# Generated by Django 3.2.3 on 2021-07-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_usuario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Imagenes'),
        ),
    ]
