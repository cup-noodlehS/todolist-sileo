from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ["text", "pub_date", "completed"]

admin.site.register(Item, ItemAdmin)