# Generated by Django 2.2.7 on 2020-04-08 12:33

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_guide_trip_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='about_me',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='age',
            field=models.IntegerField(choices=[(1, '18-25'), (2, '25-35'), (3, '35+')], default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='experience',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='free_days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Frayday'), (6, 'Saturday'), (7, 'Sunday')], default=1, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Armenian'), (2, 'English'), (3, 'France'), (4, 'Russian')], default=1, max_length=7, verbose_name='language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
