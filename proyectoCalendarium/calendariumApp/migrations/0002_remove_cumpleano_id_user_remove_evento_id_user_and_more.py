# Generated by Django 4.2.2 on 2023-06-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendariumApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cumpleano',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
