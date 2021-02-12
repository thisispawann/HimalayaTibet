# Generated by Django 3.1.5 on 2021-02-06 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productapp', '0001_initial'),
        ('umapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='blog')),
                ('content', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('nettotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='umapp.city')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='umapp.customer')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='umapp.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('order_code', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('shipping_charge', models.PositiveIntegerField(blank=True, default=50, null=True)),
                ('shipping_charge_discount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('nettotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('customer_payment_status', models.BooleanField(default=False)),
                ('requested_shipping_date', models.DateField(blank=True, null=True)),
                ('is_guest_checkout', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('street_address', models.CharField(max_length=200)),
                ('is_complete', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Ready to Ship', 'Ready to Ship'), ('OnTheWay', 'On The Way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=200)),
                ('note', models.TextField(blank=True, null=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.cart')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='umapp.city')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='umapp.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='organization')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='organization')),
                ('address', models.CharField(max_length=500)),
                ('slogan', models.CharField(blank=True, max_length=500, null=True)),
                ('contact_no', models.CharField(max_length=200)),
                ('alt_contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('map_location', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('alt_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('about_us', models.TextField()),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=200, null=True)),
                ('viber', models.CharField(blank=True, max_length=200, null=True)),
                ('seller_policy', models.TextField()),
                ('return_policy', models.TextField()),
                ('support_policy', models.TextField()),
                ('privacy_policy', models.TextField()),
                ('terms_conditions', models.TextField()),
                ('return_policy_for_products', models.TextField(blank=True, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=256, null=True)),
                ('fb_messenger_script', models.CharField(blank=True, max_length=1024, null=True)),
                ('google_analytics_script', models.CharField(blank=True, max_length=500, null=True)),
                ('fb_pixel_script', models.CharField(blank=True, max_length=4000, null=True)),
                ('detail_pixel', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='payment_methods')),
                ('merchant_code', models.CharField(blank=True, max_length=50, null=True)),
                ('test_secret_key', models.CharField(blank=True, max_length=1024, null=True)),
                ('live_secret_key', models.CharField(blank=True, max_length=1024, null=True)),
                ('test_public_key', models.CharField(blank=True, max_length=1024, null=True)),
                ('live_public_key', models.CharField(blank=True, max_length=1024, null=True)),
                ('client_js_url', models.TextField(blank=True, null=True)),
                ('test_api_endpoint', models.CharField(blank=True, max_length=200, null=True)),
                ('live_api_endpoint', models.CharField(blank=True, max_length=200, null=True)),
                ('client_config_script', models.TextField(blank=True, null=True)),
                ('payment_url', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.PositiveIntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField()),
                ('responded', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(blank=True, to='productapp.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='sliders')),
                ('action_link_name', models.CharField(blank=True, max_length=200, null=True)),
                ('action_link', models.CharField(blank=True, max_length=200, null=True)),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuotationReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('message', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.quotation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('tender', models.DecimalField(decimal_places=2, max_digits=19)),
                ('change', models.DecimalField(decimal_places=2, max_digits=19)),
                ('payment_status', models.BooleanField(default=False)),
                ('receiver_name', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.order')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.paymentmethod')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=19)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('shipping_charge', models.PositiveIntegerField(default=50)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Ready to Ship', 'Ready to Ship'), ('OnTheWay', 'On The Way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=200)),
                ('order_note', models.CharField(blank=True, max_length=512, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.cart')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
