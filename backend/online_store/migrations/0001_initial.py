# Generated by Django 4.2 on 2023-04-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('tel', models.CharField(blank=True, max_length=45, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('active_substance', models.CharField(blank=True, max_length=45, null=True)),
                ('for_children', models.IntegerField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'drugs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Provisors',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('contact_tel', models.CharField(max_length=45)),
                ('img', models.CharField(max_length=255)),
                ('provisor', models.ForeignKey(db_column='provisor', on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.authuser')),
            ],
            options={
                'db_table': 'provisors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderOfProvider',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_order', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date_of_delivery', models.DateField()),
                ('date_made', models.DateField()),
                ('delivery_mode', models.CharField(max_length=45)),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.drugs')),
                ('provider', models.ForeignKey(db_column='provider', on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.authuser')),
            ],
            options={
                'db_table': 'order_of_provider',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('number_of_order', models.CharField(max_length=45)),
                ('date_of_delivery', models.DateField()),
                ('date_made', models.DateField()),
                ('delivery_mode', models.CharField(max_length=45)),
                ('auth_user', models.ForeignKey(db_column='auth_user', on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.authuser')),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.drugs')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
    ]
