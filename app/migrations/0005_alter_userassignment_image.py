# Generated by Django 4.0.2 on 2023-11-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_prediction_userassignment_assignedletter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userassignment',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]