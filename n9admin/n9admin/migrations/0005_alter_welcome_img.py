# Generated by Django 5.1.3 on 2024-12-04 15:49

import n9admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n9admin', '0004_alter_welcome_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome',
            name='img',
            field=models.FileField(upload_to='images/', validators=[n9admin.models.validate_svg]),
        ),
    ]
