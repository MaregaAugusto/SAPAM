# Generated by Django 3.0 on 2020-09-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idrebap', models.IntegerField()),
                ('barrio_nombre', models.CharField(max_length=300)),
                ('provincia_id', models.IntegerField()),
                ('provincia_nombre', models.CharField(max_length=300)),
                ('departamento_nombre', models.CharField(max_length=300)),
                ('localidad_nombre', models.CharField(max_length=300)),
            ],
        ),
    ]