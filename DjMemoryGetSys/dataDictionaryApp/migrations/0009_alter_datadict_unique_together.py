# Generated by Django 4.2.13 on 2024-05-11 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataDictionaryApp', '0008_alter_datadict_remark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='datadict',
            unique_together={('type', 'code')},
        ),
    ]
