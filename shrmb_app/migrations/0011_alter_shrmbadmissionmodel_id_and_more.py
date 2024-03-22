# Generated by Django 5.0.3 on 2024-03-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrmb_app', '0010_alter_shrmbadmissionmodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shrmbadmissionmodel',
            name='id',
            field=models.TextField(default='619c7b3c62b74c9ba02279584d31cba2', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbdepartmentmodel',
            name='id',
            field=models.TextField(default='619c7b3c62b74c9ba02279584d31cba2', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbdoctorsmodel',
            name='id',
            field=models.TextField(default='619c7b3c62b74c9ba02279584d31cba2', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbhistorymodel',
            name='id',
            field=models.TextField(default='619c7b3c62b74c9ba02279584d31cba2', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shrmbvacanciesmodel',
            name='id',
            field=models.TextField(default='619c7b3c62b74c9ba02279584d31cba2', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
