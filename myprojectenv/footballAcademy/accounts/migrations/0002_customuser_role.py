# Generated by Django 5.0.3 on 2024-04-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('player', 'Player'), ('coach', 'Coach')], default='player', max_length=10),
        ),
    ]
