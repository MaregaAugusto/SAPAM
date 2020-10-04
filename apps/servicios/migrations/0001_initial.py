# Generated by Django 3.0 on 2020-09-26 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ancianos', '0001_initial'),
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.BooleanField(default=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('gasto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('anciano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitante', to='ancianos.Anciano')),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ayudante', to='colaboradores.Colaborador')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('estado', models.BooleanField(default=False)),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='miservicio', to='servicios.Servicio')),
            ],
        ),
    ]