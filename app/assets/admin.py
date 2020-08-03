from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    ObjectList,
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .models import Asset

@modeladmin_register
class AssetAdmin(ModelAdmin):
    model = Asset
    menu_label = "Assets"
    menu_icon = "doc-empty"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "program", "asset_type", "live")
    search_fields = ("title", "description", "program", "asset_type")
