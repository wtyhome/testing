# Generated by Django 2.2.6 on 2019-11-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0009_auto_20191031_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='活動名稱')),
                ('use_file', models.FileField(upload_to='')),
            ],
        ),
    ]
