# Generated by Django 3.2 on 2022-11-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_house_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='house_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
