# Generated by Django 5.0.2 on 2024-04-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='url',
            field=models.URLField(default='', verbose_name='Ссылка'),
        ),
    ]