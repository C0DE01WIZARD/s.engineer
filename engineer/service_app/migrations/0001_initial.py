# Generated by Django 5.0.2 on 2024-02-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название ТО')),
                ('short_description', models.CharField(default='', max_length=255, verbose_name='Короткое описание')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Техническое обслуживание',
            },
        ),
    ]
