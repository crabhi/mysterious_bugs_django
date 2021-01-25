from django.contrib import admin

from main.models import Customer, UpgradeRequest, Contract


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(UpgradeRequest)
class UpgradeRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass
