# Generated by Django 4.2.2 on 2023-06-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendariumApp', '0006_alter_tracker_realizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='realizado',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
