# Generated by Django 4.2.1 on 2023-06-07 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease_prediction', '0002_alter_prediction_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diseases',
            new_name='Disease',
        ),
    ]
