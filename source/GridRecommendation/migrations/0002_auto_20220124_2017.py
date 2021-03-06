# Generated by Django 3.2.8 on 2022-01-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GridRecommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaentry',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='mediaentry',
            name='program',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mediaentry',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mediaentry',
            name='channel',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mediaentry',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mediaentry',
            name='starting_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
