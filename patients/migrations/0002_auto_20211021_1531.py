# Generated by Django 3.1.4 on 2021-10-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_email',
            field=models.EmailField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
