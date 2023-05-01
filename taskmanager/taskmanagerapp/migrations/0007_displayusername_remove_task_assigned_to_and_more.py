# Generated by Django 4.0.6 on 2023-02-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagerapp', '0006_delete_displayusernames_task_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='displayusername',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='username',
        ),
    ]
