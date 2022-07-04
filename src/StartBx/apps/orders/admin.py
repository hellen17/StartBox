from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .actions import export_to_csv
from .models import *
# Register your models here.


#admin.site.register(PaymentOptions)



def order_detail(obj):
    url = reverse("orders:admin_order_detail", args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')


def order_pdf(obj):
    url = reverse("orders:admin_order_pdf", args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


order_pdf.short_description = "Invoice"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        # order_detail,
        # order_pdf,
        "email",
        "paid",
        "status",
        "created",
        "updated",
    ]
    list_filter = ["paid","status", "created", "updated"]
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(OrderItem)
