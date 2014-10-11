from django.contrib import admin
from nakshatra.models import Event, MajorCategory, MinorCategory, Organization, Participant,EventEnrollment, City

# Register your models here.

admin.site.register(Event)
admin.site.register(MajorCategory)
admin.site.register(MinorCategory)
admin.site.register(Organization)
admin.site.register(Participant)
admin.site.register(EventEnrollment)
admin.site.register(City)

