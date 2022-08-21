# Generated by Django 2.2 on 2022-08-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('new', 'Не модерировано'), ('moderated', 'Модерировано'), ('rejected', 'Отклонено')], default='new', max_length=15, verbose_name='Модерация'),
        ),
    ]
