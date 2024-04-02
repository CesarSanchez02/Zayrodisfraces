# Generated by Django 5.0.3 on 2024-03-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmailaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('verified', models.IntegerField()),
                ('primary', models.IntegerField()),
            ],
            options={
                'db_table': 'account_emailaddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountEmailconfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'account_emailconfirmation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsCustomuser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'accounts_customuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsCustomuserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'accounts_customuser_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsCustomuserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'accounts_customuser_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='ID_CATEGORIA', primary_key=True, serialize=False)),
                ('categoria', models.CharField(blank=True, db_column='CATEGORIA', max_length=45, null=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_comentario', models.AutoField(db_column='ID_COMENTARIO', primary_key=True, serialize=False)),
                ('comentario', models.CharField(blank=True, db_column='COMENTARIO', max_length=500, null=True)),
                ('calificacion', models.IntegerField(blank=True, db_column='CALIFICACION', null=True)),
                ('fecha', models.DateField(blank=True, db_column='FECHA', null=True)),
            ],
            options={
                'db_table': 'comentarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id_comprobante', models.AutoField(db_column='ID_COMPROBANTE', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, db_column='FECHA', null=True)),
                ('metodo_pago', models.CharField(blank=True, db_column='METODO_PAGO', max_length=45, null=True)),
                ('sub_total', models.IntegerField(blank=True, db_column='SUB_TOTAL', null=True)),
                ('precio_total', models.IntegerField(blank=True, db_column='PRECIO_TOTAL', null=True)),
            ],
            options={
                'db_table': 'comprobante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id_disponibilidad', models.AutoField(db_column='ID_DISPONIBILIDAD', primary_key=True, serialize=False)),
                ('descripcion', models.IntegerField(blank=True, db_column='DESCRIPCION', null=True)),
            ],
            options={
                'db_table': 'disponibilidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoComprobante',
            fields=[
                ('id_estado_comprobante', models.AutoField(db_column='ID_ESTADO_COMPROBANTE', primary_key=True, serialize=False)),
                ('descripcion', models.IntegerField(blank=True, db_column='DESCRIPCION', null=True)),
            ],
            options={
                'db_table': 'estado_comprobante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(db_column='ID_INVENTARIO', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, db_column='CANTIDAD', null=True)),
                ('precio_unitario', models.IntegerField(blank=True, db_column='PRECIO_UNITARIO', null=True)),
                ('entrada_producto', models.DateField(blank=True, db_column='ENTRADA_PRODUCTO', null=True)),
                ('salida_producto', models.DateField(blank=True, db_column='SALIDA_PRODUCTO', null=True)),
                ('stripe_price_id', models.CharField(blank=True, db_column='STRIPE_PRICE_ID', max_length=255, null=True)),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('id_pqrs', models.AutoField(db_column='ID_PQRS', primary_key=True, serialize=False)),
                ('numero_radicado', models.IntegerField(blank=True, db_column='NUMERO_RADICADO', null=True)),
                ('tipo_pqrs', models.CharField(blank=True, db_column='TIPO_PQRS', max_length=50, null=True)),
                ('mensaje', models.CharField(blank=True, db_column='MENSAJE', max_length=250, null=True)),
                ('imagen', models.CharField(blank=True, db_column='IMAGEN', max_length=250, null=True)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=250, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=250, null=True)),
            ],
            options={
                'db_table': 'pqrs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='ID_PRODUCTO', primary_key=True, serialize=False)),
                ('nombre_disfraz', models.CharField(blank=True, db_column='NOMBRE_DISFRAZ', max_length=45, null=True)),
                ('imagen_disfraz', models.CharField(blank=True, db_column='IMAGEN_DISFRAZ', max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, db_column='DESCRIPCION', max_length=45, null=True)),
                ('stripe_product_id', models.CharField(blank=True, db_column='STRIPE_PRODUCT_ID', max_length=255, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=191)),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
                ('extra_data', models.JSONField()),
            ],
            options={
                'db_table': 'socialaccount_socialaccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
                ('client_id', models.CharField(max_length=191)),
                ('secret', models.CharField(max_length=191)),
                ('key', models.CharField(max_length=191)),
                ('provider_id', models.CharField(max_length=200)),
                ('settings', models.JSONField()),
            ],
            options={
                'db_table': 'socialaccount_socialapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialappSites',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'socialaccount_socialapp_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialtoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('token_secret', models.TextField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socialaccount_socialtoken',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id_talla', models.AutoField(db_column='ID_TALLA', primary_key=True, serialize=False)),
                ('talla', models.CharField(blank=True, db_column='TALLA', max_length=45, null=True)),
            ],
            options={
                'db_table': 'talla',
                'managed': False,
            },
        ),
    ]
