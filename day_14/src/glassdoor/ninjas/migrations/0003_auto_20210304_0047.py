# Generated by Django 3.1.7 on 2021-03-03 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0002_auto_20210304_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='sname',
            new_name='name',
        ),
    ]
