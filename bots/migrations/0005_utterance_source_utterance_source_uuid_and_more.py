# Generated by Django 5.1.2 on 2025-01-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0004_remove_botevent_valid_event_type_event_sub_type_combinations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utterance',
            name='source',
            field=models.IntegerField(choices=[(1, 'Per Participant Audio'), (2, 'Closed Caption From Platform')], default=1),
        ),
        migrations.AddField(
            model_name='utterance',
            name='source_uuid',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='utterance',
            name='audio_format',
            field=models.IntegerField(choices=[(1, 'PCM'), (2, 'MP3')], default=1, null=True),
        ),
    ]