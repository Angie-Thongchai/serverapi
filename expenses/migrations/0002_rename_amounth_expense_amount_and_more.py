# Generated by Django 5.0.3 on 2024-03-28 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='amounth',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='decription',
            new_name='description',
        ),
    ]
