# Generated by Django 5.1.7 on 2025-03-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='idade',
        ),
        migrations.AddField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='rg',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
