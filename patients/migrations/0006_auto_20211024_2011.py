# Generated by Django 3.1.4 on 2021-10-24 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_session_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.userprofile'),
        ),
    ]
