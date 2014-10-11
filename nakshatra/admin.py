from django.contrib import admin
from nakshatra.models import Event, MajorCategory, MinorCategory

# Register your models here.

admin.site.register(Event)
admin.site.register(MajorCategory)
admin.site.register(MinorCategory)
