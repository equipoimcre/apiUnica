# Generated by Django 3.1.6 on 2021-02-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudusuario',
            name='ddbb_mysql',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudusuario',
            name='form_odk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudusuario',
            name='roll_pentajo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
