# Generated by Django 3.1.3 on 2021-05-12 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_app', '0002_deliveries'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveries',
            old_name='legbye',
            new_name='legbye_runs',
        ),
    ]
