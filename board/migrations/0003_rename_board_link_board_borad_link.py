# Generated by Django 4.1.3 on 2022-12-06 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_rename_borad_link_board_board_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="board", old_name="board_link", new_name="borad_link",
        ),
    ]
