# Generated by Django 3.1.3 on 2021-05-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_app', '0005_auto_20210516_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_model',
            name='form',
            field=models.IntegerField(),
        ),
    ]
