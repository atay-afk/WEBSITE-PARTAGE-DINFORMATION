# Generated by Django 3.1.6 on 2021-03-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncours', '0003_auto_20210304_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='salle',
            name='num_salle',
        ),
        migrations.RemoveField(
            model_name='salle',
            name='salle_type',
        ),
        migrations.RemoveField(
            model_name='salle',
            name='seance',
        ),
        migrations.AddField(
            model_name='cours',
            name='date',
            field=models.DateField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='seance',
            field=models.TimeField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='date',
            field=models.DateField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='seance',
            field=models.TimeField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='salle',
            name='nom_salle',
            field=models.CharField(max_length=40, null=True),
        ),
    ]