# Generated by Django 5.0.2 on 2024-04-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0011_systems_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='cat_id',
            field=models.IntegerField(default='1', verbose_name='Категория'),
        ),
    ]
