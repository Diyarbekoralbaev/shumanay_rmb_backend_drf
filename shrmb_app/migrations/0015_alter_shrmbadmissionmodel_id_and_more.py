# Generated by Django 5.0.3 on 2024-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrmb_app', '0014_alter_shrmbadmissionmodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shrmbadmissionmodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbdepartmentmodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbdoctorsmodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbhistorymodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbvacanciesmodel',
            name='id',
            field=models.TextField(default='fd6ccf4e225748a4b579b4701e4503ac', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]