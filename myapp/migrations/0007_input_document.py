# Generated by Django 2.2.10 on 2021-03-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_input_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
