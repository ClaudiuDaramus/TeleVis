# Generated by Django 3.2.9 on 2022-02-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchHistory', '0005_watchhistory_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchhistory',
            name='externalId',
            field=models.IntegerField(),
        ),
    ]
