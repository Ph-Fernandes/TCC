# Generated by Django 4.0.4 on 2022-07-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='payment',
            field=models.BooleanField(),
        ),
    ]
