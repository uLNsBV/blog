# Generated by Django 4.1 on 2022-09-05 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='desciption',
            new_name='description',
        ),
    ]
