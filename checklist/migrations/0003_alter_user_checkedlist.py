# Generated by Django 3.2.4 on 2021-07-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_alter_checklist_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='checkedList',
            field=models.ManyToManyField(blank=True, to='checklist.Checklist'),
        ),
    ]