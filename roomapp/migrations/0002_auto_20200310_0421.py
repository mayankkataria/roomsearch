# Generated by Django 3.0.3 on 2020-03-09 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='AppUser',
        ),
    ]
