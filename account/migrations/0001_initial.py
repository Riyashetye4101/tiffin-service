# Generated by Django 3.1.7 on 2021-05-13 16:32

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_sp', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_order', models.DateField(auto_now_add=True, null=True)),
                ('no_of_orders', models.CharField(max_length=100, null=True)),
                ('last_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.user')),
                ('phone_number', models.CharField(max_length=10)),
                ('alt_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceAnOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('out for Delivery', 'out for Delivery'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=200, null=True)),
                ('new_date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.order')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.placeanorder')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('pin_no', models.CharField(max_length=20)),
                ('Area_name', models.CharField(max_length=200)),
                ('land_mark', models.CharField(max_length=200)),
                ('building_name', models.CharField(max_length=200)),
                ('flate_number', models.CharField(max_length=100)),
                ('date_of_order', models.DateField(auto_now_add=True)),
                ('total_amount', models.FloatField(null=True)),
                ('placeanorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.placeanorder')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.user')),
                ('admin_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=10)),
                ('alt_phone_no', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('pin_no', models.CharField(max_length=20)),
                ('Area_name', models.CharField(max_length=200)),
                ('land_mark', models.CharField(max_length=200)),
                ('building_name', models.CharField(max_length=200)),
                ('flate_number', models.CharField(max_length=100)),
                ('customer', models.ManyToManyField(to='account.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='sp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.serviceprovider'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=200, null=True)),
                ('sp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.serviceprovider')),
            ],
        ),
    ]