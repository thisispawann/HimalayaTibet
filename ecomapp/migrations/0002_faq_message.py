# Generated by Django 3.1.5 on 2021-02-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField()),
                ('contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
