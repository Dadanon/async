# Generated by Django 3.0.5 on 2020-07-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200717_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at',), 'verbose_name': 'статью', 'verbose_name_plural': 'статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='reading_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Максимально - 255 символов', max_length=255, verbose_name='Заголовок'),
        ),
    ]
