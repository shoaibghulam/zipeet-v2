# Generated by Django 3.1 on 2020-08-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_auto_20200828_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_account',
            name='Service_Category_id',
        ),
        migrations.AddField(
            model_name='company_account',
            name='Service_Category',
            field=models.CharField(choices=[('product', 'Products Sale'), ('service', 'Service'), ('jobs', 'Jobs')], default='product', max_length=100),
        ),
        migrations.DeleteModel(
            name='Service_Category',
        ),
    ]