# Generated by Django 2.2.7 on 2019-11-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20191125_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
