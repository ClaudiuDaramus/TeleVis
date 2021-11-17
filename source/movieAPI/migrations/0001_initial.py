# Generated by Django 3.2.8 on 2021-11-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
                ('rated', models.CharField(max_length=10)),
                ('released', models.DateField()),
                ('runtime', models.IntegerField(null=True)),
                ('director', models.CharField(max_length=20, null=True)),
                ('plot', models.CharField(max_length=1500)),
                ('actors', models.ManyToManyField(to='movieAPI.Actor')),
                ('genres', models.ManyToManyField(to='movieAPI.Genre')),
                ('writers', models.ManyToManyField(to='movieAPI.Writer')),
            ],
        ),
    ]