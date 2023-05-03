# Generated by Django 3.1.6 on 2021-03-31 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncours', '0012_emploi_enseignant'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='duree',
            field=models.IntegerField(blank='true', null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestioncours.enseignant'),
        ),
    ]
