# Generated by Django 4.2.7 on 2023-11-25 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_categorias_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='catProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorias'),
        ),
    ]