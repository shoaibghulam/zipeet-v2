# Generated by Django 3.1 on 2020-08-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200304_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_offers',
            field=models.CharField(choices=[('weeklyoffer', 'Weekly Offers'), ('hotoffers', 'Hot offers'), ('Nooffer', 'No Offer')], default='Nooffer', max_length=120),
        ),
    ]