# Generated by Django 4.1.1 on 2022-09-27 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_review_author_alter_review_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.film', verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
