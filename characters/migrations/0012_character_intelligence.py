# Generated by Django 3.0.5 on 2020-05-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20200522_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.CharField(default='0', max_length=254),
        ),
    ]