from django.contrib import admin


from ap_gestorPedidos.models import Clientes,Articulos,Pedidos
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","tfon")
    search_fields = ("nombre","tfon")
    list_filter = ("nombre",)

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero','fecha','entregado']
    list_filter = ['fecha']
    date_hierarchy = "fecha"
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidoAdmin)
