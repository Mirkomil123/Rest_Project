# Generated by Django 4.2.7 on 2023-11-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='expires_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]