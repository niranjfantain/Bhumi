from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('E', 'Either'),

)

EVENT_TYPE = (
    ('I', 'Indivigual'),
    ('G', 'Group'),
)

CATEGORY_LEVEL = (
    ('S', 'Senior'),
    ('SS', 'Super Senior'),
    ('J', 'Junior'),
)


class MainCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Main Category Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    class Meta:
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"

    def __unicode__(self):
        return unicode(self.name)


class SubCategory(models.Model):
    mainCategory = models.ForeignKey(
        MainCategory,
        verbose_name="Main Category"
    )
    name = models.CharField(
        max_length=50,
        verbose_name="Sub Category Name"
    )
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __unicode__(self):
        return unicode(self.name)


class Country(models.Model):
    name = models.CharField(max_length=150, verbose_name="Country Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return unicode(self.name)


class State(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name="Country"
    )
    name = models.CharField(max_length=150, verbose_name="State Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)


class City(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name="Country"
    )
    state = ChainedForeignKey(
        State,
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        verbose_name="State"
    )
    name = models.CharField(max_length=75, verbose_name="City Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __unicode__(self):
        return unicode(self.name)


class Location(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name="Country"
    )
    state = ChainedForeignKey(
        State,
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        verbose_name="State"
    )
    city = ChainedForeignKey(
        City,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        verbose_name="City"
    )
    name = models.CharField(max_length=150, verbose_name="Location Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)


class Venue(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name="Country"
    )
    state = ChainedForeignKey(
        State,
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        verbose_name="State"
    )
    city = ChainedForeignKey(
        City,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        verbose_name="City"
    )
    name = models.CharField(max_length=150, verbose_name="Venue Name")
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)


class Organization(models.Model):
    name = models.CharField(max_length=75, verbose_name="Organization Name")
    regNo = models.CharField(
        max_length=75,
        verbose_name="Registration Number",
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        verbose_name="Country"
    )
    state = ChainedForeignKey(
        State,
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        verbose_name="State"
    )
    city = ChainedForeignKey(
        City,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        verbose_name="City"
    )
    address = models.TextField(max_length=75, verbose_name="Address")
    landmark = models.CharField(max_length=75, verbose_name="Landmark")
    orgContact = models.IntegerField(
        max_length=15,
        verbose_name="Organization Contact Number"
    )
    email = models.EmailField(
        max_length=75,
        verbose_name="Email-Id",
        null=True,
        blank=True
    )
    email1 = models.EmailField(
        max_length=75,
        verbose_name="Alternative Email-Id",
        null=True,
        blank=True
    )
    website = models.URLField(
        max_length=100,
        verbose_name="Website",
        null=True,
        blank=True
    )
    contactName = models.CharField(
        max_length=75,
        verbose_name="Primary Person Name"
    )
    contactDesignation = models.CharField(
        max_length=75,
        verbose_name="Primary Person Designation"
    )
    contact = models.IntegerField(
        max_length=15,
        verbose_name="Primary Person Contact-Number"
    )
    contactName1 = models.CharField(
        max_length=75,
        verbose_name="Alternative Person Name",
        null=True,
        blank=True
    )
    contactDesignation1 = models.CharField(
        max_length=75,
        verbose_name="Alternative Person Designation",
        null=True,
        blank=True
    )
    contact1 = models.IntegerField(
        max_length=15,
        verbose_name="Alternative Person Contact-Number",
        null=True,
        blank=True
    )
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)


class Participant(models.Model):
    name = models.CharField(max_length=75, verbose_name="Name")
    dob = models.DateField(verbose_name="Date Of Birth")
    age = models.IntegerField(
        default=0,
        verbose_name="Age",
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='M',
        verbose_name='Gender'
    )
    grade = models.IntegerField(
        verbose_name="Class",
        null=True,
        blank=True
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_LEVEL,
        default='J',
        verbose_name='Category'
    )
    image = models.ImageField(
        max_length=100,
        null=True,
        blank=True
    )
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)


class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.TextField(max_length=150, verbose_name="Description")
    datetime = models.DateTimeField(verbose_name="Description")
    venue = models.ForeignKey(Venue, verbose_name="Venue")
    coordinator = models.ForeignKey(User)
    mainCategory = models.ForeignKey(
        MainCategory,
        verbose_name="Main Category"
    )
    subCategory = ChainedForeignKey(
        SubCategory,
        chained_field="mainCategory",
        chained_model_field="mainCategory",
        show_all=False,
        auto_choose=True,
        verbose_name="Sub Category"
    )
    applicableGender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='M',
        verbose_name='Gender'
    )
    eventype = models.CharField(
        max_length=2,
        choices=EVENT_TYPE,
        default='I',
        verbose_name='Event Type'
    )
    createdOn = models.DateTimeField(
        verbose_name="created Date",
        auto_now_add=True
    )
    updatedOn = models.DateTimeField(
        verbose_name="Updated Date",
        auto_now=True
    )

    def __unicode__(self):
        return unicode(self.name)
