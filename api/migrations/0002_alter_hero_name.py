# Generated by Django 4.2.1 on 2023-05-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
