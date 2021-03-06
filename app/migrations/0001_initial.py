# Generated by Django 3.2.10 on 2021-12-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('distance', models.PositiveIntegerField(verbose_name='Дистанция')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'SAP',
                'verbose_name_plural': "SAP's",
            },
        ),
    ]
