# Generated by Django 3.0.5 on 2020-04-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
