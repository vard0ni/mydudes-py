# Generated by Django 3.2.18 on 2023-06-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230614_1757'),
        ('userauths', '0003_alter_profile_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='groups', to='core.Group'),
        ),
    ]
