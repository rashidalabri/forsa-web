from django.contrib import admin

from misfa.models import Source, Entry, EntryValue

admin.site.register(Source)
admin.site.register(Entry)
admin.site.register(EntryValue)