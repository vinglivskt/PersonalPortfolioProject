# Generated by Django 4.2.6 on 2023-10-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
