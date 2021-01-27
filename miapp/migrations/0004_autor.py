# Generated by Django 3.1.5 on 2021-01-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_auto_20210113_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=110)),
                ('apellido', models.CharField(max_length=110)),
                ('sexo', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('pais', models.CharField(max_length=20)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]