# Generated by Django 4.2.3 on 2023-07-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisement',
        ),
    ]
