# Generated by Django 3.1.6 on 2021-02-17 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qa',
            old_name='reciever',
            new_name='owner',
        ),
    ]
