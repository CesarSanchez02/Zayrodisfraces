from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from django.utils.formats import number_format
from pages.models import Categoria, Talla, Disponibilidad, Producto, Inventario, Comentarios, Comprobante, EstadoComprobante, Pqrs
import stripe
from import_export import resources
from import_export.admin import ImportExportModelAdmin

stripe.api_key = settings.STRIPE_SECRET_KEY


class InventarioAdmin(ImportExportModelAdmin):
    
    def nombre_disfraz(self, obj):
        return obj.id_producto.nombre_disfraz
    
    def imagen_disfraz(self, obj):
        if obj.id_producto.imagen_disfraz:
            if settings.AWS_STORAGE_BUCKET_NAME:
                return format_html('<img src="https://{}/{}" style="max-height: 50px; max-width: 50px;" />'.format(
                    settings.AWS_S3_CUSTOM_DOMAIN,
                    obj.id_producto.imagen_disfraz
                ))
            else:
                return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.id_producto.imagen_disfraz.url))
        else:
            return ""
    
    def categoria(self, obj):
        return obj.id_producto.id_categoria.categoria
    
    def talla(self, obj):
        return obj.id_producto.id_talla.talla
    
    def formatted_precio_unitario(self, obj):
        return f"${number_format(obj.precio_unitario, 0, force_grouping=True)}"
    formatted_precio_unitario.short_description = 'Precio Unitario (COP)'
    
    def descripcion_display(self, obj):
        return str(obj.id_disponibilidad)
    descripcion_display.short_description = 'Disponibilidad'

    list_display = ('nombre_disfraz', 'imagen_disfraz', 'categoria', 'talla', 'cantidad', 'formatted_precio_unitario', 'entrada_producto', 'salida_producto', 'descripcion_display')
    list_filter = ('id_disponibilidad',)

    exclude = ('stripe_product_id', 'stripe_price_id')
    actions = ['nodisponible_selected', 'enable_selected']
    
    def nodisponible_selected(self, request, queryset):
        queryset.update(id_disponibilidad=Disponibilidad.objects.filter(descripcion=False).first())

        for inventario in queryset:
            try:
                producto = inventario.id_producto
                stripe_product_id = producto.stripe_product_id

                if stripe_product_id:
                    stripe.Product.modify(
                        stripe_product_id,
                        metadata={'disponibilidad': 'No disponible'},
                    )
            except stripe.error.StripeError as e:
                print(f"Stripe Error: {e}")

    nodisponible_selected.short_description = "Marcar producto/s no disponible/s"
    
    def enable_selected(self, request, queryset):
        queryset.update(id_disponibilidad=Disponibilidad.objects.filter(descripcion=True).first())

        for inventario in queryset:
            try:
                producto = inventario.id_producto
                stripe_product_id = producto.stripe_product_id

                if stripe_product_id:
                    stripe.Product.modify(
                        stripe_product_id,
                        metadata={'disponibilidad': 'Disponible'},
                    )
            except stripe.error.StripeError as e:
                print(f"Stripe Error: {e}")

    enable_selected.short_description = "Marcar producto/s disponible/s"
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['enable_disable_buttons'] = {
            'enable': True,  # Set to True to show the enable button
            'disable': True,  # Set to True to show the disable button
        }
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class ProductoAdmin(ImportExportModelAdmin):
    list_display = ('nombre_disfraz', 'imagen_display', 'descripcion', 'id_categoria', 'id_talla')
    search_fields = ('nombre_disfraz', 'descripcion')
    exclude = ('stripe_product_id', 'stripe_price_id')

    def imagen_display(self, obj):
        if obj.imagen_disfraz:
            if settings.AWS_STORAGE_BUCKET_NAME:
                return format_html('<img src="https://{}/{}" style="max-height: 50px; max-width: 50px;" />'.format(
                    settings.AWS_S3_CUSTOM_DOMAIN,
                    obj.imagen_disfraz
                ))
            else:
                return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.imagen_disfraz.url))
        else:
            return ""

    imagen_display.short_description = 'Imagen'


class ProductResource(resources.ModelResource):
    class Meta:
        model = Producto
        fields = ('name', 'price')
        #export_order = ('name', 'price', 'category')

class PqrsAdmin(ImportExportModelAdmin):
    list_display = ('numero_radicado', 'tipo_pqrs', 'mensaje', 'nombre', 'email', 'imagen_display')

    def imagen_display(self, obj):
        if obj.imagen:
            if settings.AWS_STORAGE_BUCKET_NAME:
                return format_html('<img src="https://{}/{}" style="max-height: 50px; max-width: 50px;" />'.format(
                    settings.AWS_S3_CUSTOM_DOMAIN,
                    obj.imagen
                ))
            else:
                return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.imagen.url))
        else:
            return ""

    imagen_display.short_description = 'Imagen'

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

class DisponibilidadAdmin(ImportExportModelAdmin):
    list_display = ('id_disponibilidad', 'descripcion')


class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ('id_categoria', 'categoria')


class TallaAdmin(ImportExportModelAdmin):
    list_display = ('id_talla', 'talla')


class ComentariosAdmin(ImportExportModelAdmin):
    list_display = ('id_comentario', 'id_producto', 'comentario', 'calificacion', 'fecha')

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

class ComprobanteAdmin(ImportExportModelAdmin):
    list_display = ('id_comprobante', 'id_inventario', 'metodo_pago', 'customuser', 'fecha', 'precio_total', 'id_estado_comprobante')
    actions = ['mark_as_paid', 'mark_as_unpaid']

    def estado_comprobante_display(self, obj):
        return obj.id_estado_comprobante.descripcion
    estado_comprobante_display.short_description = 'Estado'

    def mark_as_paid(self, request, queryset):
        queryset.update(id_estado_comprobante=EstadoComprobante.objects.get(descripcion='Pagado'))

    mark_as_paid.short_description = "Marcar como Pagado"

    def mark_as_unpaid(self, request, queryset):
        queryset.update(id_estado_comprobante=EstadoComprobante.objects.get(descripcion='No pagado'))

    mark_as_unpaid.short_description = "Marcar como No pagado"

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

class EstadoComprobanteAdmin(ImportExportModelAdmin):
    list_display = ('id_estado_comprobante', 'descripcion')

admin.site.register(Pqrs, PqrsAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Talla, TallaAdmin)
admin.site.register(Disponibilidad, DisponibilidadAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Comprobante, ComprobanteAdmin)
admin.site.register(EstadoComprobante, EstadoComprobanteAdmin)
admin.site.register(Inventario, InventarioAdmin)