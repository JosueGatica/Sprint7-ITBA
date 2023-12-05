# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class MarcaTarjeta(models.Model):
    marcatarjeta = models.TextField(db_column='marcaTarjeta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarcaTarjeta'


class Tarjeta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.TextField(db_column='Numero', unique=True, blank=True, null=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    fechaotorgamiento = models.DateField(db_column='FechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='FechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    tipotarjeta = models.TextField(db_column='TipoTarjeta', blank=True, null=True)  # Field name made lowercase.
    marcatarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, db_column='marcaTarjeta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjeta'


class TipoCliente(models.Model):
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'TipoCliente'


class TipoCuenta(models.Model):
    tipocuenta = models.TextField(db_column='tipoCuenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoCuenta'


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField()
    new_id = models.AutoField(primary_key=True)
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.IntegerField()
    new_type = models.IntegerField()
    user_action = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.BinaryField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipocliente = models.ForeignKey(TipoCliente, models.DO_NOTHING, db_column='tipoCliente', blank=True, null=True)  # Field name made lowercase.
    tarjeta = models.ForeignKey(Tarjeta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipocuenta = models.IntegerField(db_column='tipoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Movimientos(models.Model):
    numero_cuenta = models.IntegerField()
    monto = models.IntegerField()
    tipo_operacion = models.TextField()
    hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'


from django.db import models
from django.contrib.auth.models import User

class Prestamo(models.Model):
    TIPO_CHOICES = [
        ('BLACK', 'Black'),
        ('GOLD', 'Gold'),
        ('CLASSIC', 'Classic'),
    ]

    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=10, choices=TIPO_CHOICES)
    loan_date = models.DateField()
    loan_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Calcula el monto preaprobado según el tipo de cliente
        if self.loan_type == 'BLACK':
            self.loan_total = 500000
        elif self.loan_type == 'GOLD':
            self.loan_total = 300000
        elif self.loan_type == 'CLASSIC':
            self.loan_total = 100000

        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'prestamo'



class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'
