# Generated by Django 2.2.11 on 2020-06-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True, verbose_name='message')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
            ],
        ),
    ]