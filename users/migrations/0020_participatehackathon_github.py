# Generated by Django 3.0.5 on 2023-02-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20230218_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatehackathon',
            name='github',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
