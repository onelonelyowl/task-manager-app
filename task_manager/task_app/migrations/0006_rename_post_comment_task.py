# Generated by Django 4.2.7 on 2023-12-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0005_alter_task_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='task',
        ),
    ]
