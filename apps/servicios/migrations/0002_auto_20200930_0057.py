# Generated by Django 3.0 on 2020-09-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='gasto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]