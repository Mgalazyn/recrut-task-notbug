# Generated by Django 4.1.4 on 2023-02-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_entries_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
