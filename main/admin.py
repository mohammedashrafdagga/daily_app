from django.contrib import admin
from .models import DailyNotes
# Register your models here.


class DailyNotesAdmin(admin.ModelAdmin):

    list_display = ('serial_number', 'user_owner', 'title')


admin.site.register(DailyNotes, DailyNotesAdmin)
