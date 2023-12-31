# Generated by Django 4.2.6 on 2023-10-24 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quality_of_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.IntegerField(verbose_name='Качество обслуживания')),
            ],
            options={
                'verbose_name': 'Качество обслуживания',
                'verbose_name_plural': 'Качество обслуживания',
            },
        ),
        migrations.CreateModel(
            name='Service_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names_company', models.CharField(max_length=50, verbose_name='Название компании')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Номер договора')),
                ('company_director', models.CharField(max_length=100, verbose_name='ФИО директора компании')),
                ('quality_of_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.quality_of_service', verbose_name='Качество обслуживания от 1 до 5')),
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
                ('location', models.CharField(max_length=50, verbose_name='Местонахождение')),
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
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.systems', verbose_name='Выберите систему')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
            },
        ),
    ]
