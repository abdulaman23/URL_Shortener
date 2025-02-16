# Generated by Django 5.1.4 on 2025-02-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('short_url', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('long_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
