from django.contrib import admin
from .models import TaskLocation, CustomerLocation, TaskerLocation, MapLocation

admin.site.register(TaskerLocation)
admin.site.register(MapLocation)
admin.site.register(TaskLocation)
admin.site.register(CustomerLocation)

# Register your models here.
