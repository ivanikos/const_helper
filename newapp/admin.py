from django.contrib import admin
from .models import joint




class jointAdmin(admin.ModelAdmin):
    list_display = ('line', 'isometric', 'locationweld', 'numberjoint', 'dateweld')
    list_display_links = ('isometric', 'line')
    search_fields = ('title', 'isometric')
# Register your models here.
admin.site.register(joint, jointAdmin)