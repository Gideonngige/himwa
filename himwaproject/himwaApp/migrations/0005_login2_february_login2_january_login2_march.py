# Generated by Django 5.0.6 on 2024-05-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himwaApp', '0004_login2_paid_alter_login2_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='login2',
            name='february',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='login2',
            name='january',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='login2',
            name='march',
            field=models.PositiveIntegerField(default=0.0),
        ),
    ]
