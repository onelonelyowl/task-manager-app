# Generated by Django 4.2.7 on 2023-12-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=1500, verbose_name='Task description'),
        ),
    ]
