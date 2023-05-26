# Generated by Django 4.2.1 on 2023-05-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0003_publichollydays_region_delete_publichollidays'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.region', verbose_name='Region'),
            preserve_default=False,
        ),
    ]
