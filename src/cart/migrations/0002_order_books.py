from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(blank=True, to='cart.bookinorder'),
        ),
    ]