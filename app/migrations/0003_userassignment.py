# Generated by Django 4.0.2 on 2023-11-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_usersubmission_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('prediction', models.CharField(blank=True, max_length=50)),
                ('feedback', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
