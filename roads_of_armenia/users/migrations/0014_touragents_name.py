# Generated by Django 2.2.7 on 2020-03-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200312_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='touragents',
            name='name',
            field=models.CharField(default='new', max_length=255),
            preserve_default=False,
        ),
    ]
