from django.contrib import admin

# Register your models here.
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.urls import path

from calculator.models import ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    change_list_template = "sync_rates.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('sync_rates/', self.sync_rates), ]
        return my_urls + urls

    def sync_rates(self, request):
        # call django command
        call_command('exchangerate')
        self.message_user(request, "Rates are synced")
        return HttpResponseRedirect("../")


