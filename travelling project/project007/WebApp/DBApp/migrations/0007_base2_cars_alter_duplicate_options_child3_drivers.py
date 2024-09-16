# Generated by Django 5.0.3 on 2024-04-19 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBApp', '0006_duplicate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base2',
            fields=[
                ('empno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('car_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('car_model', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='duplicate',
            options={'ordering': ['-salary']},
        ),
        migrations.CreateModel(
            name='Child3',
            fields=[
                ('base2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DBApp.base2')),
                ('address', models.CharField(max_length=100)),
            ],
            bases=('DBApp.base2',),
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('license_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('cars', models.ManyToManyField(to='DBApp.cars')),
            ],
        ),
    ]