# Generated by Django 4.2.7 on 2023-11-25 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProducto', models.CharField(max_length=50)),
                ('desProducto', models.CharField(max_length=200)),
                ('catProducto', models.CharField(max_length=20)),
                ('canProducto', models.PositiveIntegerField(default=True)),
                ('precioProducto', models.PositiveBigIntegerField(default=True)),
                ('estProducto', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=20)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
            ],
        ),
        migrations.DeleteModel(
            name='Programmer',
        ),
        migrations.AddField(
            model_name='productos',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.proveedores'),
        ),
    ]
