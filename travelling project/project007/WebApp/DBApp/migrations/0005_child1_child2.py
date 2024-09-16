# Generated by Django 5.0.3 on 2024-04-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBApp', '0004_adhar_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child1',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('phno', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Child2',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=130)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]