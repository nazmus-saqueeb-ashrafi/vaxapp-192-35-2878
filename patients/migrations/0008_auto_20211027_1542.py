# Generated by Django 3.1.4 on 2021-10-27 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20211027_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.userprofile'),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_vaccinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.vaccinator'),
        ),
    ]