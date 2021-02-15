from django.contrib import admin

# Register your models here.

from .models import Venue
from .models import ClubUser
from .models import Event


admin.site.register(Venue)
admin.site.register(ClubUser)
admin.site.register(Event)