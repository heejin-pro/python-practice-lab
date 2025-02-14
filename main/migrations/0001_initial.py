# Generated by Django 4.1.3 on 2022-11-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='사용자 아이디')),
                ('user_password', models.CharField(max_length=100, verbose_name='사용자 비밀번호')),
                ('user_nickname', models.CharField(max_length=100, verbose_name='사용자 별명')),
                ('user_level', models.IntegerField(default=0, verbose_name='사용자 레벨')),
                ('user_experience', models.IntegerField(default=0, verbose_name='사용자 경험치')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
