# Generated by Django 2.2.7 on 2019-11-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20191125_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.BinaryField(),
        ),
    ]
