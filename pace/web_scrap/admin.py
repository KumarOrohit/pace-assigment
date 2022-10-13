from django.contrib import admin
from .models import WebScrapData
# Register your models here.


@admin.register(WebScrapData)
class WebScrapDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', "h1", "h24", "d7", "d7", "market_cap", "volume_24h", "circulating_supply")
    search_fields = ('name',)