# Generated by Django 5.0 on 2023-12-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itbank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('ciudad', models.TextField(blank=True, null=True)),
                ('estado', models.TextField(blank=True, null=True)),
                ('codigo_postal', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'direcciones',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuditoriaCuenta',
        ),
        migrations.DeleteModel(
            name='Movimientos',
        ),
        migrations.AlterModelTable(
            name='marcatarjeta',
            table='marcaTarjeta',
        ),
        migrations.AlterModelTable(
            name='tarjeta',
            table='tarjeta',
        ),
        migrations.AlterModelTable(
            name='tipocliente',
            table='tipoCliente',
        ),
        migrations.AlterModelTable(
            name='tipocuenta',
            table='tipoCuenta',
        ),
    ]
