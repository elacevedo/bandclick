# Generated by Django 2.2 on 2019-04-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='some bio string', max_length=1000),
        ),
    ]
