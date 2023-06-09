# Generated by Django 4.2.1 on 2023-05-13 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_hero_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.BooleanField()),
                ('fonte', models.CharField(max_length=45)),
                ('titulo', models.CharField(max_length=50)),
                ('noticias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.noticia')),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
