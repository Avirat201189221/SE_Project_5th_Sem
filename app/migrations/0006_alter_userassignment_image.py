# Generated by Django 4.0.2 on 2023-11-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_userassignment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userassignment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
