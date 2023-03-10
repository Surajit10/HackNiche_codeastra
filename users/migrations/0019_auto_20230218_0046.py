# Generated by Django 3.0.5 on 2023-02-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20230217_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatehackathon',
            name='designation',
            field=models.TextField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='experience',
            field=models.TextField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='languages_used',
            field=models.TextField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='no_of_exp',
            field=models.TextField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='no_of_repos',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='no_of_stars',
            field=models.IntegerField(default=0, max_length=400),
        ),
        migrations.AddField(
            model_name='participatehackathon',
            name='skills',
            field=models.TextField(default=0, max_length=400),
        ),
    ]
