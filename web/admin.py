from django.contrib import admin
from web.models import *
from import_export import resources


class GoodsResources(resources.ModelResource):
    class Meta:
        model = Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    import_export_args = {'import_resource_class': GoodsResources, 'export_resource_class': GoodsResources}

    list_display = [
        'brand', 'Gmodel', 'unit', 'type', 'price', 'min_price', 'meno', 'supplier', 'user', 'date',]
    search_fields = ['Gmodel', 'meno',]
    # list_display_links = [ 'Gmodel', ]
    list_filter = ['brand', 'type']
    list_per_page = 15
    resource_class = GoodsResources

    # list_editable = ['price', 'min_price', ]
    ordering = ['-date', ]


@admin.register(Model_record)
class Model_recordAdmin(admin.ModelAdmin):
    list_display = ['id', 'sk_model', 'sp_model', 'supplier', 'meno', ]
    search_fields = ['sk_model', 'sp_model']
    list_filter = ['sk_model', 'sp_model', 'supplier']
    list_display_links = ['sk_model', 'sp_model', ]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel', 'phone', 'contact', ]
    search_fields = ['name', 'contact']
    list_filter = ['name', 'contact', 'tel']
    list_display_links = ['name', 'tel', 'phone', 'contact', ]
    # list_editable =['name','desc']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'date', ]
    search_fields = ['title', 'details']
    list_filter = ['title', ]
    # list_display_links = ['title', 'details']
    # list_editable = ['name', ]

    style_fields = {
        'details': "mdeditor"
    }

admin.site.site_header = '斯康企业管理平台0.1'
admin.site.site_title = '斯康企业管理平台0.1'