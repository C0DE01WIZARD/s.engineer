# Generated by Django 5.0.2 on 2024-04-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0006_purchase_defect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase',
            field=models.CharField(max_length=50, verbose_name='Наименование материала или услуги'),
        ),
    ]
