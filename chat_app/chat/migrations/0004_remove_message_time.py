# Generated by Django 4.0.3 on 2022-04-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_time_alter_message_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='time',
        ),
    ]
