# Generated by Django 5.0.3 on 2024-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_alter_newsmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
