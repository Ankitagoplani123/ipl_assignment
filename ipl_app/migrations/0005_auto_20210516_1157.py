# Generated by Django 3.1.3 on 2021-05-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_app', '0004_temp_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_model',
            name='form',
            field=models.IntegerField(choices=[('2008', 2008), ('2009', 2009), ('2010', 2010), ('2011', 2011), ('2012', 2012), ('2013', 2013), ('2014', 2014), ('2015', 2015), ('2016', 2016), ('2017', 2017)]),
        ),
    ]
