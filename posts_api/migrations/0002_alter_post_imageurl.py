# Generated by Django 4.1.5 on 2023-01-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageURL',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
