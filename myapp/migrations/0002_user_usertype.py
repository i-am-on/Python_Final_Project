# Generated by Django 5.0.6 on 2024-05-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='Buyer', max_length=100),
        ),
    ]
