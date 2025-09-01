from django.db import models


class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    prv_empresa = models.CharField(max_length=40)
    prv_giro = models.CharField(max_length=20)
    prv_contacto = models.CharField(max_length=30)
    prv_direccion = models.CharField(max_length=60)
    prv_pco_postal = models.CharField(max_length=10)
    prv_telefono = models.CharField(max_length=24)

    def __str__(self):
        return self.prv_empresa


class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=15)
    cat_desc = models.TextField()
    cat_foto = models.BinaryField()

    def __str__(self):
        return self.cat_nombre


class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    id_categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )
    pro_nombre = models.CharField(max_length=40)
    pro_descripcion = models.CharField(max_length=30)
    pro_precio = models.DecimalField(max_digits=19, decimal_places=4)
    pro_stock = models.IntegerField()

    def __str__(self):
        return self.pro_nombre


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=5)
    cli_nombre = models.CharField(max_length=40)
    cli_contacto = models.CharField(max_length=30, null=True, blank=True)
    cli_titulo_contacto = models.CharField(max_length=30, null=True, blank=True)
    cli_direccion = models.CharField(max_length=60, null=True, blank=True)
    cli_ciudad = models.CharField(max_length=15, null=True, blank=True)
    cli_region = models.CharField(max_length=15, null=True, blank=True)
    cli_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    cli_pais = models.CharField(max_length=15, null=True, blank=True)
    cli_telefono = models.CharField(max_length=24, null=True, blank=True)
    cli_mail = models.CharField(max_length=24, null=True, blank=True)

    def __str__(self):
        return f"{self.cli_nombre} ({self.id_cliente})"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    emp_nombre = models.CharField(max_length=20)
    emp_apellido = models.CharField(max_length=10)
    emp_titulo = models.CharField(max_length=30, null=True, blank=True)
    emp_mail = models.EmailField(max_length=25, null=True, blank=True)
    emp_fechanac = models.DateField(null=True, blank=True)
    emp_fecha_contrato = models.DateField(null=True, blank=True)
    emp_direccion = models.CharField(max_length=80, null=True, blank=True)
    emp_celular = models.CharField(max_length=24, null=True, blank=True)
    emp_foto = models.BinaryField(null=True, blank=True)
    emp_notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.emp_nombre} {self.emp_apellido} (ID: {self.id_empleado})"


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        db_column='id_cliente',
        related_name="ordenes"
    )
    id_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        db_column='id_empleado',
        related_name="ordenes"
    )
    ord_fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Orden {self.id_orden} - Cliente {self.id_cliente_id}"


class DetalleOrden(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE,
        db_column='id_orden',
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto',
        related_name="detalles"
    )
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Orden {self.orden.id_orden} - Producto {self.producto.id_producto} (x{self.cantidad})"

