# Generated by Django 4.1.1 on 2022-09-27 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_film_options_alter_film_duration_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
