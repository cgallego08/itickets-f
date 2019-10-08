# Generated by Django 2.2.5 on 2019-10-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ticket', models.CharField(max_length=250)),
                ('precio_ticket', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cantidad_ticket', models.IntegerField()),
                ('descripcion_ticket', models.CharField(max_length=250)),
            ],
        ),
    ]