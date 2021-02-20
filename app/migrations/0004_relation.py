# Generated by Django 2.1.15 on 2021-02-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210220_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='نام')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='مشخصات')),
                ('input', models.ManyToManyField(blank=True, null=True, to='app.Material', verbose_name=' قطعه ورودی ')),
                ('output', models.ManyToManyField(blank=True, null=True, to='app.Station', verbose_name=' قطعه خروجی ')),
            ],
            options={
                'verbose_name': 'ارتبات',
                'verbose_name_plural': 'ارتباتاط',
            },
        ),
    ]
