# Generated by Django 3.0.4 on 2020-04-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.TextField(max_length=1000),
        ),
    ]