# Generated by Django 4.1.2 on 2023-06-27 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
    ]