# Generated by Django 2.2.7 on 2020-04-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_guide_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='car_availability',
            field=models.BooleanField(default=False),
        ),
    ]