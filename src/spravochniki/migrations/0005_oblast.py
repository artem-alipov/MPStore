# Generated by Django 4.2.1 on 2023-05-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0004_city_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oblast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Oblast name')),
            ],
        ),
    ]