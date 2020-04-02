from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Activity

@modeladmin_register
class ActivityAdmin(ModelAdmin):
    model = Activity
    menu_label = "Activity"
    menu_icon = "form"
    menu_order = 210
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "overview_copy", "program")
    search_fields = ("title", "overview_copy", "program", "activity_type", "tag")
