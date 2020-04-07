from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Asset

@modeladmin_register
class AssetAdmin(ModelAdmin):
    model = Asset
    menu_label = "Assets"
    menu_icon = "doc-empty"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "program", "asset_type")
    search_fields = ("title", "description", "program", "asset_type")