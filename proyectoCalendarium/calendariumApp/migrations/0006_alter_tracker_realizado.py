# Generated by Django 4.2.2 on 2023-06-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendariumApp', '0005_alter_tracker_realizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='realizado',
            field=models.CharField(max_length=1),
        ),
    ]
