# Generated by Django 5.1.3 on 2024-12-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n9admin', '0005_alter_welcome_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=550)),
                ('msg', models.CharField(max_length=550)),
                ('desc', models.CharField(max_length=550)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
