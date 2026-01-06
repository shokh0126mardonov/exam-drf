from django.contrib import admin

from .models import Doctor,Patient,TImeSlot

admin.site.register([Doctor,TImeSlot,Patient])