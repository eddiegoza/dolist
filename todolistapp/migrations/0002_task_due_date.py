# Generated by Django 4.1.7 on 2023-05-10 19:50

from django.db import migrations, models
import todolistapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=todolistapp.models.one_week_hence),
        ),
    ]