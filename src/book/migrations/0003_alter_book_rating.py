# Generated by Django 4.2.1 on 2023-06-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_book_name_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=255, verbose_name='Rating'),
        ),
    ]