# Generated by Django 2.2.4 on 2024-07-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0009_auto_20240719_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
