# Generated by Django 3.1.7 on 2021-02-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cart_user_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
