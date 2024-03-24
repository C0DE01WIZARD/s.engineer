# Generated by Django 5.0.2 on 2024-02-23 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=55, verbose_name='Тип зданий')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Quality_of_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(verbose_name='Качество обслуживания')),
            ],
            options={
                'verbose_name': 'Качество обслуживания',
                'verbose_name_plural': 'Качество обслуживания',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=255, verbose_name='Задача')),
                ('datetime', models.DateTimeField(verbose_name='Выполнить до')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=55, verbose_name='Жилой комплекс, Социальный объект, Коммерческое здание')),
                ('year_of_construction_start', models.IntegerField(verbose_name='Год начала строительства')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.building_type', verbose_name='Класс зданий')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('settlement', models.CharField(max_length=50, verbose_name='Поселение')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('home', models.CharField(max_length=50, verbose_name='Дом')),
                ('corps', models.CharField(max_length=50, verbose_name='Корпус')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.location', verbose_name='Выберите локацию')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Service_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names_company', models.CharField(max_length=50, verbose_name='Название компании')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Номер договора')),
                ('company_director', models.CharField(max_length=100, verbose_name='ФИО директора компании')),
                ('quality_of_service', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='systems.quality_of_service', verbose_name='Качество обслуживания от 1 до 5')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=50, verbose_name='Наименование системы')),
                ('title', models.TextField(max_length=500, verbose_name='Описание')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное название')),
                ('location', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='systems.location', verbose_name='Локация')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.service_company', verbose_name='Сервисная компания по обслуживанию')),
            ],
            options={
                'verbose_name': 'Система',
                'verbose_name_plural': 'Системы',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=50, verbose_name='Название оборудования')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Производитель')),
                ('model', models.CharField(max_length=50, verbose_name='Модель оборудования')),
                ('year', models.IntegerField(verbose_name='Год ввода в эксплуатацию')),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.address', verbose_name='Адрес')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='systems.systems', verbose_name='Выберите систему')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
            },
        ),
    ]
