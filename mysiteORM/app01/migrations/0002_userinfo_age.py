# Generated by Django 2.2.12 on 2021-10-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
