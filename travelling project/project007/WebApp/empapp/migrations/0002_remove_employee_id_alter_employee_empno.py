# Generated by Django 5.0.3 on 2024-04-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='empno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
