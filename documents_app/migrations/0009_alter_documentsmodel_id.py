# Generated by Django 5.0.3 on 2024-03-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents_app', '0008_alter_documentsmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='id',
            field=models.TextField(default='e753dec06736482f8838cd4247966f73', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
