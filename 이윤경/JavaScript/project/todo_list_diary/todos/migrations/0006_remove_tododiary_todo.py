# Generated by Django 3.2.12 on 2022-03-18 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_alter_tododiary_todos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tododiary',
            name='todo',
        ),
    ]
