# Generated by Django 3.1.7 on 2021-03-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0003_auto_20210304_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.IntegerField(max_length=50),
        ),
    ]
