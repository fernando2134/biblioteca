# Generated by Django 4.1.3 on 2022-11-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='recommended_age',
            field=models.CharField(max_length=6),
        ),
    ]
