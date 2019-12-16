# Generated by Django 2.2.6 on 2019-11-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0010_activity_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_data',
            name='name_id',
            field=models.CharField(default=1, max_length=10, verbose_name='活動代碼'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity_data',
            name='use_file',
            field=models.FileField(upload_to='', verbose_name='上傳檔案'),
        ),
    ]