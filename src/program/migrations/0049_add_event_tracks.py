# Generated by Django 2.0.4 on 2018-05-12 14:29

from django.db import migrations

def add_event_tracks(apps, schema_editor):
    Camp = apps.get_model('camps', 'Camp')
    EventTrack = apps.get_model('program', 'EventTrack')
    EventProposal = apps.get_model('program', 'EventProposal')
    Event = apps.get_model('program', 'Event')
    for camp in Camp.objects.all():
        # create the default track for this camp
        track = EventTrack.objects.create(
            name="BornHack",
            slug="bornhack",
            camp=camp
        )
        Event.objects.filter(camp=camp).update(track=track)
        EventProposal.objects.filter(camp=camp).update(track=track)


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0048_auto_20180512_1625'),
    ]

    operations = [
        migrations.RunPython(add_event_tracks),
    ]
