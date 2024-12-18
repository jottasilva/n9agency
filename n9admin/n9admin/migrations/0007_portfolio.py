# Generated by Django 5.1.3 on 2024-12-04 18:35

import n9admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n9admin', '0006_idea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=380)),
                ('desc', models.CharField(max_length=8880)),
                ('img', models.FileField(upload_to='images-portfolio/', validators=[n9admin.models.validate_svg])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('specs', models.CharField(max_length=280)),
            ],
        ),
    ]
