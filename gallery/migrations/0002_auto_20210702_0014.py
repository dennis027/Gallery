# Generated by Django 3.2.5 on 2021-07-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
