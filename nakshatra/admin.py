from django.contrib import admin
from nakshatra.models import MainCategory, SubCategory, \
    Country, State, City, Location, Venue, Organization, \
    Participant, Event


class MainCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('mainCategory', 'name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class StateAdmin(admin.ModelAdmin):
    fields = ('country', 'name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class CityAdmin(admin.ModelAdmin):
    fields = (('country', 'state'), 'name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class LocationAdmin(admin.ModelAdmin):
    fields = (('country', 'state', 'city'), 'name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class VenueAdmin(admin.ModelAdmin):
    fields = (('country', 'state', 'city'), 'name',)
    list_display = ('name',)
    exclude = ('createdOn', 'updatedOn',)


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('name', 'regNo', 'country', 'state', 'city', 'address',
              'landmark', 'orgContact', 'email', 'email1', 'website',
              'contactName', 'contactDesignation', 'contact',
              'contactName1', 'contactDesignation1', 'contact1',
              )
    list_display = ('name', 'address', 'landmark', 'contactName', 'contact')
    exclude = ('createdOn', 'updatedOn',)


class ParticipantAdmin(admin.ModelAdmin):
    fields = ('name', 'dob', 'age', 'gender', 'grade', 'category', 'image')
    readonly_fields = ('age', 'category')
    list_display = ('name', 'age', 'gender', 'category', 'image')
    exclude = ('createdOn', 'updatedOn',)


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'datetime', 'venue', 'coordinator',
              'mainCategory', 'subCategory', 'applicableGender', 'eventype',
              )
    list_display = ('name', 'datetime', 'venue', 'coordinator',)
    exclude = ('createdOn', 'updatedOn',)


admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
