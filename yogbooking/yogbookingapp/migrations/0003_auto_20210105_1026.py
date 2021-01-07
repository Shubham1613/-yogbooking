# Generated by Django 3.0.7 on 2021-01-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogbookingapp', '0002_auto_20210102_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img1',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img2',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='profile',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='resume',
            field=models.FileField(upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
