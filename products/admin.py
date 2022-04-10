from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Category, Product, SKU, Generation


admin.site.site_header = "Pro-pharma Admin"
admin.site.site_title = "Pro-pharma Admin"
admin.site.index_title = "Pro-pharma Administration"
admin.empty_value_display = "**Empty**"


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "quantity",
        "created_at",
    )


class SKUResource(resources.ModelResource):
    class Meta:
        model = SKU
        fields = (
            "product__name",
            "serial_number",
        )


@admin.register(SKU)
class SKUModelAdmin(ImportExportModelAdmin):
    resource_class = SKUResource
    list_display = (
        "product",
        "serial_number",
    )
    list_filter = ("product__name", "created_at",)


@admin.register(Generation)
class GenerationModelAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "quantity",
        "created_at",
    )
