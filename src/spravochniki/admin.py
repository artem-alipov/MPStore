from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.City)
admin.site.register(models.PublicHollydays)
admin.site.register(models.Region)
admin.site.register(models.Oblast)