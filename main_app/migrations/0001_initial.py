# Generated by Django 5.0 on 2023-12-13 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
                ('countries', models.ManyToManyField(to='main_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='Drinking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Drank')),
                ('sweetness', models.CharField(choices=[('B', 'Bitter'), ('D', 'Dry'), ('S', 'Sweet'), ('VS', 'Very Sweet')], default='B', max_length=2)),
                ('review', models.CharField(max_length=250)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.wine')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
