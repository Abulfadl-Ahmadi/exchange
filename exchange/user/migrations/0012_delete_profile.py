# Generated by Django 4.1.1 on 2022-11-28 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_profile_followerscount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]