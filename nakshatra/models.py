from django.db import models

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

EVENT_TYPE = (
    ('I', 'Indivigual'),
    ('G', 'Group'),
)


class MajorCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Major Category Name")


class MinorCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Minor Category Name")


class Location(models.Model):
    name = models.CharField(max_length=150, verbose_name="Location Name")


class City(models.Model):
    name = models.CharField(max_length=75, verbose_name="City Name")
    location = models.ForeignKey(
        Location,
        verbose_name="Location Name"
    )


class Event(models.Model):
    eventName = models.CharField(max_length=50, verbose_name="Event Name")
    desc = models.TextField(max_length=150, verbose_name="Description")
    majorCategory = models.ForeignKey(
        MajorCategory,
        verbose_name="Major Category"
    )
    minorCategory = models.ForeignKey(
        MinorCategory,
        verbose_name="Minor Category"
    )
    eventType = models.CharField(
        max_length=2,
        choices=EVENT_TYPE,
        default='I',
        verbose_name='Event Type'
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='M',
        verbose_name='Gender'
    )
    city = models.ForeignKey(
        City,
        default=None,
        verbose_name="City Name"
    )
    minP = models.IntegerField(default=None, verbose_name="Minimum Participant")
    maxP = models.IntegerField(default=None, verbose_name="Maximum Participant")