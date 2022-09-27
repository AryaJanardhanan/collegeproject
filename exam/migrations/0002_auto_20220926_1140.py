# Generated by Django 3.0.5 on 2022-09-26 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0007_online_status'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_name',
        ),
        migrations.AddField(
            model_name='course',
            name='portion_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clgapp.Portions'),
        ),
    ]
