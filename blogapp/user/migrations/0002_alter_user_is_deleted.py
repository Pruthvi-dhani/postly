# Generated by Django 5.2 on 2025-04-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
