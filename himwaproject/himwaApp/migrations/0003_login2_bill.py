# Generated by Django 5.0.6 on 2024-05-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himwaApp', '0002_login2_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='login2',
            name='bill',
            field=models.IntegerField(default=0.0),
        ),
    ]
