# Generated by Django 3.2.5 on 2021-07-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
        ),
    ]
