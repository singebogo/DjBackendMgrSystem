# Generated by Django 4.2.13 on 2024-05-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeType',
            fields=[
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updatedDate', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('createdUser', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='创建者')),
                ('updatedUser', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='更新者')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('invildId', models.BooleanField(default=True, verbose_name='状态')),
                ('enableTime', models.DateTimeField(null=True, verbose_name='生效时间')),
                ('disableTime', models.DateTimeField(null=True, verbose_name='失效时间')),
            ],
            options={
                'verbose_name': '基础配置类型',
                'db_table': 'codetype',
            },
        ),
    ]
