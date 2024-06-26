# Generated by Django 5.0.2 on 2024-04-17 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0002_defect'),
        ('systems', '0014_systems_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defect',
            options={'verbose_name': 'Неисправность', 'verbose_name_plural': 'Неисправности'},
        ),
        migrations.AddField(
            model_name='defect',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.equipment', verbose_name='Выберите оборудование'),
        ),
    ]
