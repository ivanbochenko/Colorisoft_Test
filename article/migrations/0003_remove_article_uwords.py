# Generated by Django 2.0.6 on 2018-06-06 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180606_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='uwords',
        ),
    ]
