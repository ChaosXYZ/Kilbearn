# Generated by Django 2.2.5 on 2020-03-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBapp', '0005_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icons',
            name='icon',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]
