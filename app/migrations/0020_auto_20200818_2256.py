# Generated by Django 3.1 on 2020-08-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_product_product_offers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Category',
            fields=[
                ('Service_Category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('product', 'Products Sale'), ('Sevice', 'Service'), ('Jobs', 'Jobs')], default='product', max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='mypic', upload_to='Products/'),
        ),
    ]