# Generated by Django 3.1 on 2020-08-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_order_ordertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Ordertime',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]