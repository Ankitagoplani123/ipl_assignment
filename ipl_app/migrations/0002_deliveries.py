# Generated by Django 3.1.3 on 2021-05-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=50)),
                ('bowling_team', models.CharField(max_length=50)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=50)),
                ('non_striker', models.CharField(max_length=50)),
                ('bowler', models.CharField(max_length=50)),
                ('is_super_over', models.IntegerField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(max_length=50)),
                ('dismissal_kind', models.CharField(max_length=50)),
                ('fielder', models.CharField(max_length=50)),
            ],
        ),
    ]
