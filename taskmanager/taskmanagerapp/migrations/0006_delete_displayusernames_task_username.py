# Generated by Django 4.0.6 on 2023-02-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagerapp', '0005_displayusernames_task_assigned_to'),
    ]

    operations = [
        migrations.DeleteModel(
            name='displayusernames',
        ),
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
