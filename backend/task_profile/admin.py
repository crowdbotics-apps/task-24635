from django.contrib import admin
from .models import TaskerProfile, InviteCode, CustomerProfile, Notification

admin.site.register(TaskerProfile)
admin.site.register(CustomerProfile)
admin.site.register(Notification)
admin.site.register(InviteCode)

# Register your models here.
