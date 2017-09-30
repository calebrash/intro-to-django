from django.contrib import admin

from djtest.models import Customer, Invoice

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    ordering = ('name',)
    list_display = (
        'name',
        'email',
        'customer_type',
    )

class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = (
        'customer',
        'amount',
    )
    readonly_fields = (
        'created_at',
    )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
