from django.contrib import admin

# Register your models here.
from zone.models import Zone


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'zone_type', 'is_showing')


admin.site.register(Zone, ZoneAdmin)
