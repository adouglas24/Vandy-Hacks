# Generated by Django 3.0.7 on 2020-07-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
