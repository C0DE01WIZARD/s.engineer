# Generated by Django 5.0.2 on 2024-04-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0010_alter_addarticle_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addarticle',
            name='url',
            field=models.SlugField(max_length=150, null=True),
        ),
    ]
