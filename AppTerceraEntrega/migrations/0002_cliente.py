# Generated by Django 4.2.4 on 2023-09-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTerceraEntrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
    ]
