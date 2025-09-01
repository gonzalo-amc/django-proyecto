from django.contrib import admin
from .models import Cliente, Empleado, Orden, DetalleOrden, Producto, Proveedor, Categoria


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_cliente', 'cli_nombre', 'cli_contacto', 'cli_titulo_contacto',
        'cli_direccion', 'cli_ciudad', 'cli_region', 'cli_codigo_postal',
        'cli_pais', 'cli_telefono', 'cli_mail'
    )
    search_fields = ('cli_nombre', 'cli_contacto', 'cli_ciudad', 'cli_pais', 'cli_mail')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id_empleado', 'emp_nombre', 'emp_apellido', 'emp_titulo',
        'emp_mail', 'emp_fechanac', 'emp_fecha_contrato', 'emp_direccion',
        'emp_celular'
    )
    search_fields = ('emp_nombre', 'emp_apellido', 'emp_mail')


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'id_cliente', 'id_empleado', 'ord_fecha')
    list_filter = ('ord_fecha',)
    search_fields = ('id_cliente__cli_nombre', 'id_empleado__emp_nombre')


@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'orden', 'producto', 'cantidad', 'precio_unitario', 'descuento')
    search_fields = ('orden__id_orden', 'producto__pro_nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto', 'id_categoria', 'pro_nombre', 'pro_descripcion',
        'pro_precio', 'pro_stock'
    )
    search_fields = ('pro_nombre', 'pro_descripcion', 'id_categoria__cat_nombre')


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'id_proveedor', 'prv_empresa', 'prv_giro', 'prv_contacto',
        'prv_direccion', 'prv_pco_postal', 'prv_telefono'
    )
    search_fields = ('prv_empresa', 'prv_giro', 'prv_contacto')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'cat_nombre', 'cat_desc')
    search_fields = ('cat_nombre', 'cat_desc')
