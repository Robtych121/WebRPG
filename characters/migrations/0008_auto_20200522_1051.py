# Generated by Django 3.0.5 on 2020-05-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20200521_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.CharField(default='18', max_length=254),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.CharField(default='18', max_length=254),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.CharField(default='18', max_length=254),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.CharField(default='19', max_length=254),
        ),
        migrations.AlterField(
            model_name='character',
            name='wisdom',
            field=models.CharField(default='18', max_length=254),
        ),
    ]
