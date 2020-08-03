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

from .models import Activity

@modeladmin_register
class ActivityAdmin(ModelAdmin):
    model = Activity
    menu_label = "Activity"
    menu_icon = "form"
    menu_order = 210
    add_to_settings_menu = False
    exclude_from_explorer = False
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "program", "live")
    search_fields = ("title", "overview_copy", "program", "activity_type", "tag")
