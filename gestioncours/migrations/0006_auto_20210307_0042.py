# Generated by Django 3.1.6 on 2021-03-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncours', '0005_auto_20210307_0041'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='salle',
            name='nom_salle',
            field=models.CharField(default='', max_length=40),
        ),
    ]