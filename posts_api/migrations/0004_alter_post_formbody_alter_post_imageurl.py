# Generated by Django 4.1.5 on 2023-01-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0003_alter_post_formbody_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='formBody',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='imageURL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
