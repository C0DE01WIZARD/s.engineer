# Generated by Django 5.0.2 on 2024-03-24 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0004_addarticle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addarticle',
            name='image',
        ),
    ]