# Generated by Django 3.1.7 on 2021-05-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210514_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(null=True),
        ),
    ]
