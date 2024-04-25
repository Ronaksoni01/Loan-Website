# Generated by Django 5.0 on 2024-01-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('mobile', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('subject', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
