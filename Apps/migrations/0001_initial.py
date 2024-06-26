# Generated by Django 5.0 on 2024-01-27 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('maximum_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('minimum_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('minimum_credit_score', models.PositiveIntegerField()),
                ('repayment_terms', models.PositiveIntegerField(help_text='In months')),
                ('required_documents', models.TextField(help_text='List of required documents')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('employment_status', models.CharField(max_length=50)),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=12)),
                ('credit_score', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('duration_months', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('coapplicant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('coapplicant_income', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.customer')),
                ('loan_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.loanproduct')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='blogs', to='Apps.tag')),
            ],
        ),
    ]
