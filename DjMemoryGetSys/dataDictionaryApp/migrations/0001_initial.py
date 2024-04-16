# Generated by Django 4.2.11 on 2024-04-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间')),
                ('updatedDate', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('createdUser', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='创建者')),
                ('udpatedUser', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='更新者')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('type', models.CharField(max_length=100, verbose_name='字典类型')),
                ('name', models.CharField(max_length=100, verbose_name='字典名称')),
                ('enableTime', models.DateTimeField(blank=True, null=True, verbose_name='生效时间')),
                ('disableTime', models.DateTimeField(blank=True, null=True, verbose_name='失效时间')),
                ('invildId', models.CharField(max_length=100, verbose_name='状态')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
