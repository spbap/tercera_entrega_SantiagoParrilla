# Generated by Django 5.0.8 on 2024-08-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0002_alter_pedido_persona_alter_pedido_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(),
        ),
    ]
