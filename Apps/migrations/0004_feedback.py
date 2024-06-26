# Generated by Django 5.0 on 2024-01-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0003_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME_AS_ON_PANCARD', models.CharField(max_length=20)),
                ('PERSONAL_EMAIL_ID', models.CharField(max_length=20)),
                ('MOBILE_NUMBER', models.IntegerField()),
                ('SUBJECT_LINE', models.CharField(max_length=20)),
                ('Write_Message', models.BooleanField(default=True)),
            ],
        ),
    ]
