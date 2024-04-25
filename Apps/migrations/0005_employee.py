# Generated by Django 5.0 on 2024-01-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('dept', models.IntegerField()),
                ('role', models.CharField(max_length=20)),
                ('bonus', models.IntegerField()),
            ],
        ),
    ]