# Generated by Django 3.2.5 on 2021-09-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
    ]
