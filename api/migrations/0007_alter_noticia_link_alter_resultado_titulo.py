# Generated by Django 4.1.9 on 2023-11-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_noticia_table_alter_resultado_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='titulo',
            field=models.TextField(),
        ),
    ]
