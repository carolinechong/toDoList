# Generated by Django 2.1.7 on 2019-04-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_remove_todo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='item',
            field=models.CharField(max_length=200),
        ),
    ]
