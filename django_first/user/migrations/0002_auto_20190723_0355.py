# Generated by Django 2.2.3 on 2019-07-23 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='prof_pic',
            new_name='picture',
        ),
    ]
