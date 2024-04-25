# Generated by Django 5.0 on 2024-01-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Write_Message',
            field=models.BooleanField(),
        ),
    ]
