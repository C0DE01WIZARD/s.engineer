# Generated by Django 5.0.2 on 2024-04-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0013_systems_cat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='systems',
            name='image',
            field=models.ImageField(default='изображение любого формата', null=True, upload_to='systems/', verbose_name='Изображение'),
        ),
    ]