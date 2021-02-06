# Generated by Django 3.1.6 on 2021-02-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210205_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioaplicacion',
            name='aplicacion',
        ),
        migrations.RemoveField(
            model_name='usuarioaplicacion',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='solicitudusuario',
            name='estado_solicitud',
            field=models.CharField(choices=[('1', 'Socitado'), ('2', 'Aceptado'), ('3', 'Rechazado'), ('4', 'Tramitado')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Aplicacion',
        ),
        migrations.DeleteModel(
            name='EstadoSolicitud',
        ),
        migrations.DeleteModel(
            name='UsuarioAplicacion',
        ),
    ]
