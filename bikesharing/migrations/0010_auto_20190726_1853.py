# Generated by Django 2.2.3 on 2019-07-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0009_auto_20190726_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='unlock_key',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
