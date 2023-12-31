# Generated by Django 4.2.6 on 2023-10-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='address',
            name='corps',
            field=models.CharField(max_length=50, null=True, verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='address',
            name='home',
            field=models.CharField(max_length=50, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='address',
            name='settlement',
            field=models.CharField(max_length=50, null=True, verbose_name='Поселение'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=50, null=True, verbose_name='Улица'),
        ),
    ]
