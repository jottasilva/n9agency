# Generated by Django 5.1.3 on 2024-12-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n9admin', '0007_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientArchives',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=180)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=4000)),
                ('specifications', models.CharField(max_length=4000)),
                ('archive', models.CharField(max_length=280)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(upload_to='images-portfolio/'),
        ),
    ]
