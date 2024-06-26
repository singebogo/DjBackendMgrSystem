# Generated by Django 4.2.11 on 2024-04-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataDictionaryApp', '0002_alter_datadict_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadict',
            name='code',
            field=models.CharField(default='', max_length=100, verbose_name='字典代码'),
        ),
        migrations.AddField(
            model_name='datadict',
            name='value',
            field=models.CharField(default='', max_length=100, verbose_name='字典值'),
        ),
        migrations.AlterField(
            model_name='datadict',
            name='invildId',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='datadict',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='字典名称'),
        ),
    ]
