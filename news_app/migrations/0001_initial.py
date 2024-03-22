# Generated by Django 5.0.3 on 2024-03-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.TextField(default='8501ce5fa340435b8be06903a8519a5c', editable=False, primary_key=True, serialize=False, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='draft', max_length=10)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, unique=True, upload_to='images')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
