# Generated by Django 4.1 on 2022-09-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_description_alter_car_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
