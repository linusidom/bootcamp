# Generated by Django 3.0.5 on 2020-04-27 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]