# Generated by Django 4.2.11 on 2024-04-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataDictionaryApp', '0007_alter_datadict_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadict',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
    ]
