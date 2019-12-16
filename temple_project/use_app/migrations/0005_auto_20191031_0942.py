# Generated by Django 2.2.6 on 2019-10-31 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0004_people_data_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people_data',
            name='birthday',
            field=models.DateTimeField(verbose_name='西元生日(ex:2012-01-01)'),
        ),
        migrations.AlterField(
            model_name='people_data',
            name='home_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='use_app.Home', verbose_name='選擇家庭電話'),
        ),
    ]