# Generated by Django 5.0.2 on 2024-04-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0003_status_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'verbose_name': 'Сервис', 'verbose_name_plural': 'Сервисы'},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Название сервиса'),
        ),
    ]
