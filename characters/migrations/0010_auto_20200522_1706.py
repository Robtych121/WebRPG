# Generated by Django 3.0.5 on 2020-05-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20200522_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='appearance',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]
