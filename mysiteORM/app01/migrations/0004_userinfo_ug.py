# Generated by Django 2.2.12 on 2021-10-28 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_usergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
    ]
