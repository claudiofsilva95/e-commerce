# Generated by Django 3.2.5 on 2021-07-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210724_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/%d/%m/%Y/'),
        ),
    ]
