# Generated by Django 4.0.2 on 2023-11-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_usertest_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertest',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]