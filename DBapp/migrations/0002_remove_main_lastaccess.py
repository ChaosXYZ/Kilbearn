# Generated by Django 2.2.5 on 2020-02-17 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='LastAccess',
        ),
    ]
