# Generated by Django 2.2.6 on 2019-10-29 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='address',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='home',
            name='home_phone',
            field=models.CharField(max_length=9, verbose_name='家庭電話'),
        ),
        migrations.CreateModel(
            name='People_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='輸入姓名')),
                ('birthday', models.DateTimeField(verbose_name='西元生日(ex:20120101)')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32, verbose_name='性別')),
                ('home_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='use_app.Home', verbose_name='選擇家庭電話')),
            ],
        ),
    ]
