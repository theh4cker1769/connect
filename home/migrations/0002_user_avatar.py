# Generated by Django 4.0.1 on 2022-02-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars.svg', null=True, upload_to=''),
        ),
    ]
