# Generated by Django 5.0.3 on 2024-03-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_newsmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='id',
            field=models.TextField(default='1d822f3d059241ecad26c470df903ef9', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
