from django.contrib import admin
# import models here
from .models import Finch, Sighting, Predator

# Register your models here.
admin.site.register(Finch)
admin.site.register(Sighting)
admin.site.register(Predator)