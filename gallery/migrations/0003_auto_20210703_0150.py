# Generated by Django 3.2.5 on 2021-07-02 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210702_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
    ]
