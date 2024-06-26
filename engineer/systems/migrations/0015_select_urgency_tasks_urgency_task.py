# Generated by Django 5.0.2 on 2024-04-21 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0014_systems_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select_urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgency', models.CharField(max_length=20, verbose_name='Срочность задачи')),
            ],
        ),
        migrations.AddField(
            model_name='tasks',
            name='urgency_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.select_urgency', verbose_name='Срочность'),
        ),
    ]
