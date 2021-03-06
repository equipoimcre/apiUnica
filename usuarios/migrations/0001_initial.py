# Generated by Django 3.1.6 on 2021-02-05 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activa', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Aplicacion',
                'verbose_name_plural': 'Aplicaciones',
            },
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'EstadoSolicitud',
                'verbose_name_plural': 'Estado Solicitudes',
            },
        ),
        migrations.CreateModel(
            name='UsuarioAplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.BooleanField()),
                ('aplicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.aplicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=100)),
                ('clave', fernet_fields.fields.EncryptedCharField(max_length=100)),
                ('fecha_solcitud', models.DateTimeField(auto_now_add=True)),
                ('user_mysql', models.BooleanField()),
                ('ddbb_mysql', models.TextField()),
                ('user_pentajo', models.BooleanField()),
                ('roll_pentajo', models.TextField()),
                ('user_odk', models.BooleanField()),
                ('form_odk', models.TextField()),
                ('estado_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.estadosolicitud')),
            ],
            options={
                'verbose_name_plural': 'Solicitud de usuarios',
            },
        ),
    ]
