# Generated by Django 2.2 on 2021-07-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='MEDIA/'),
        ),
    ]
