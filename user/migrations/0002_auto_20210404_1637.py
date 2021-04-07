# Generated by Django 3.1.7 on 2021-04-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '서비스 사용자', 'verbose_name_plural': '서비스 사용자'},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록시간'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, verbose_name='유저명'),
        ),
    ]