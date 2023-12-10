from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipocliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='tipoCliente', blank=True, null=True)  # Field name made lowercase.
    tarjeta = models.ForeignKey('Tarjeta', models.DO_NOTHING, db_column='tarjeta', to_field='numero', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self) -> str:
        return self.customer_name + ' ' + self.customer_surname


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipocuenta = models.ForeignKey('Tipocuenta', models.DO_NOTHING, db_column='tipoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    direccion = models.TextField()
    ciudad = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    codigo_postal = models.TextField(blank=True, null=True)
    cliente_direccion = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_direccion', blank=True, null=True)
    empleado_direccion = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'
    
    def __str__(self) -> str:
        return self.direccion

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.DateField(blank=True, null=True)
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    direccion_empleado = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='direccion_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'

    def __str__(self) -> str:
        return self.employee_name + ' ' + self.employee_surname


class Marcatarjeta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcaTarjeta'

    def __str__(self) -> str:
        return self.marca


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

    def __str__(self) -> str:
        return self.loan_id


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion_sucursal = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='direccion_sucursal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'

    def __str__(self) -> str:
        return self.branch_name


class Tarjeta(models.Model):
    numero = models.TextField(db_column='Numero', unique=True, blank=True, null=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    fechaotorgamiento = models.DateField(db_column='FechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='FechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    tipotarjeta = models.TextField(db_column='TipoTarjeta', blank=True, null=True)  # Field name made lowercase.
    marcatarjeta = models.ForeignKey(Marcatarjeta, models.DO_NOTHING, db_column='marcaTarjeta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarjeta'
    
    


class Tipocliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoCliente'

    def __str__(self) -> str:
        return self.tipo


class Tipocuenta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipoCuenta'

    def __str__(self) -> str:
        return self.tipo