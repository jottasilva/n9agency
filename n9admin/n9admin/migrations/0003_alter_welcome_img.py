# Generated by Django 5.1.3 on 2024-12-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n9admin', '0002_welcome_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome',
            name='img',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]