# Generated by Django 4.1.2 on 2023-06-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_remove_usuario_id_rol_delete_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
