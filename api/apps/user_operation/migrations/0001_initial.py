# Generated by Django 2.2.4 on 2019-08-17 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地域')),
                ('province', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='県')),
                ('city', models.CharField(default='', max_length=100, verbose_name='city')),
                ('address', models.CharField(default='', max_length=100, verbose_name='お届け先住所')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='受取人名前')),
                ('signer_mobile', models.CharField(default='', max_length=20, verbose_name='受取人番号')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
            ],
            options={
                'verbose_name': 'ユーザーお届け先',
                'verbose_name_plural': 'ユーザーお届け先',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
            ],
            options={
                'verbose_name': 'ユーザーお気に入り',
                'verbose_name_plural': 'ユーザーお気に入り',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.IntegerField(choices=[(1, '一般メッセージ'), (2, '苦情'), (3, '質問'), (4, '保障問い合わせ'), (5, '追加注文関連')], default=1, help_text='メッセージタイプ:1(一般メッセージ),2(苦情),3(質問),4(保障問い合わせ),5(追加注文関連)', verbose_name='メッセージタイプ')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='テーマ')),
                ('message', models.TextField(default='', help_text='メッセージ内容', verbose_name='メッセージ内容')),
                ('file', models.FileField(help_text='アップロードファイル', upload_to='message/images/', verbose_name='アップロードファイル')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
            ],
            options={
                'verbose_name': 'ユーザーメッセージ',
                'verbose_name_plural': 'ユーザーメッセージ',
            },
        ),
    ]