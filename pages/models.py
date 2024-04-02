from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def upload_producto(instance, filename):
    unique_suffix = get_random_string(length=6)
    extension = filename.split('.')[-1]
    new_filename = f"{instance.nombre_disfraz}_{unique_suffix}.{extension}"
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{new_filename}"

def upload_pqrs(instance, filename):
    unique_suffix = get_random_string(length=6)
    extension = filename.split('.')[-1]
    new_filename = f"{instance.numero_radicado}_{unique_suffix}.{extension}"
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{new_filename}"


class AccountEmailaddress(models.Model):
    email = models.CharField(max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AccountsCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'
        unique_together = (('user', 'email'),)


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountsCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_customuser'

    def __str__(self):
        return self.first_name + " " + self.last_name

class AccountsCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AccountsCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.categoria

class Comentarios(models.Model):
    id_comentario = models.AutoField(db_column='ID_COMENTARIO', primary_key=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='COMENTARIO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    calificacion = models.IntegerField(db_column='CALIFICACION', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentarios'
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.comentario

class Comprobante(models.Model):
    id_comprobante = models.AutoField(db_column='ID_COMPROBANTE', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    metodo_pago = models.CharField(db_column='METODO_PAGO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sub_total = models.IntegerField(db_column='SUB_TOTAL', blank=True, null=True)  # Field name made lowercase.
    precio_total = models.IntegerField(db_column='PRECIO_TOTAL', blank=True, null=True)  # Field name made lowercase.
    id_inventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='ID_INVENTARIO', blank=True, null=True)  # Field name made lowercase.
    id_estado_comprobante = models.ForeignKey('EstadoComprobante', models.DO_NOTHING, db_column='ID_ESTADO_COMPROBANTE', blank=True, null=True)  # Field name made lowercase.
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprobante'


class Disponibilidad(models.Model):
    id_disponibilidad = models.AutoField(db_column='ID_DISPONIBILIDAD', primary_key=True)  # Field name made lowercase.
    descripcion = models.BooleanField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disponibilidad'
        verbose_name_plural = "Disponibilidad"

    def __str__(self):
        return "Disponible" if self.descripcion else "No Disponible"

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EstadoComprobante(models.Model):
    id_estado_comprobante = models.AutoField(db_column='ID_ESTADO_COMPROBANTE', primary_key=True)  # Field name made lowercase.
    descripcion = models.BooleanField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_comprobante'

    def __str__(self):
        return "Pagado" if self.descripcion else "No Pagado"


class Inventario(models.Model):
    id_inventario = models.AutoField(db_column='ID_INVENTARIO', primary_key=True)
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)
    precio_unitario = models.IntegerField(db_column='PRECIO_UNITARIO', blank=True, null=True)
    entrada_producto = models.DateField(db_column='ENTRADA_PRODUCTO', blank=True, null=True)
    salida_producto = models.DateField(db_column='SALIDA_PRODUCTO', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO', blank=True, null=True)
    id_disponibilidad = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='ID_DISPONIBILIDAD', blank=True, null=True)
    stripe_price_id = models.CharField(db_column='STRIPE_PRICE_ID', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'
        verbose_name_plural = "Inventario"

    def __str__(self):
        return self.id_producto.nombre_disfraz

    def save(self, *args, **kwargs):
        try:
            producto = self.id_producto
            stripe_price_id = self.stripe_price_id

            # Call the original save method to save the changes to the database
            super().save(*args, **kwargs)

            # Get the existing Stripe product ID
            stripe_product_id = producto.stripe_product_id
            image_url = "https://{}/{}".format(settings.AWS_S3_CUSTOM_DOMAIN, producto.imagen_disfraz)

            # Update the product details in Stripe
            if stripe_product_id:
                stripe.Product.modify(
                    stripe_product_id,
                    name=producto.nombre_disfraz,
                    metadata={
                        'categoria': str(producto.id_categoria),
                        'talla': str(producto.id_talla),
                        'descripcion': producto.descripcion,
                        'cantidad': self.cantidad,
                        'disponibilidad': str(self.id_disponibilidad),
                    },
                    images=[image_url],
                )
            else:
                # If the product doesn't exist in Stripe, create it
                stripe_product = stripe.Product.create(
                    name=producto.nombre_disfraz,
                    metadata={
                        'categoria': str(producto.id_categoria),
                        'talla': str(producto.id_talla),
                        'descripcion': producto.descripcion,
                        'cantidad': self.cantidad,
                        'disponibilidad': str(self.id_disponibilidad),
                        # Add more metadata fields as needed
                    },
                    images=[image_url],
                )
                stripe_product_id = stripe_product.id
                producto.stripe_product_id = stripe_product_id
                producto.save()

            # Create new Stripe price
            stripe_price = stripe.Price.create(
                product=stripe_product_id,
                unit_amount=int(self.precio_unitario * 100), 
                currency='cop'  # Adjust currency as needed
            )

            # Update stripe_price_id in the database
            self.stripe_price_id = stripe_price.id
            super().save(*args, **kwargs)

        except stripe.error.StripeError as e:
            # Handle Stripe errors here
            print(f"Stripe Error: {e}")


class Pqrs(models.Model):
    id_pqrs = models.AutoField(db_column='ID_PQRS', primary_key=True)  # Field name made lowercase.
    numero_radicado = models.IntegerField(db_column='NUMERO_RADICADO', blank=True, null=True)  # Field name made lowercase.
    tipo_pqrs = models.CharField(db_column='TIPO_PQRS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mensaje = models.CharField(db_column='MENSAJE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    imagen = models.ImageField(db_column='IMAGEN', upload_to=upload_pqrs, blank=True, null=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pqrs'
        verbose_name_plural = "PQRS"

    def __str__(self):
        return self.numero_radicado

class Producto(models.Model):
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    nombre_disfraz = models.CharField(db_column='NOMBRE_DISFRAZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagen_disfraz = models.ImageField(upload_to=upload_producto)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='ID_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    id_talla = models.ForeignKey('Talla', models.DO_NOTHING, db_column='ID_TALLA', blank=True, null=True)  # Field name made lowercase.
    stripe_product_id = models.CharField(db_column='STRIPE_PRODUCT_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return str(self.nombre_disfraz)


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=200)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.JSONField()
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=200)
    settings = models.JSONField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Talla(models.Model):
    id_talla = models.AutoField(db_column='ID_TALLA', primary_key=True)  # Field name made lowercase.
    talla = models.CharField(db_column='TALLA', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talla'

    def __str__(self):
        return self.talla