# Generated by Django 4.0.2 on 2023-11-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_usertest_time_secs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertest',
            name='time_secs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
