# Generated by Django 4.2 on 2024-11-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
