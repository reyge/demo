# Generated by Django 3.0.6 on 2020-05-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=20)),
                ('finish_date', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=50)),
                ('uni', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=20)),
                ('finish_date', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('rate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Myinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=20)),
                ('fb', models.CharField(max_length=1028)),
                ('instagram', models.CharField(max_length=1028)),
                ('linkedin', models.CharField(max_length=1028)),
                ('dob', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]
