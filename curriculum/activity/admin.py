from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)

from .models import GuidedReading, DataTask, MiniLesson, TakeAction

class GuidedReadingAdmin(ModelAdmin):
    model = GuidedReading
    menu_label = "Guided Reading"
    menu_icon = "doc-empty"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "overview_copy", "program")
    search_fields = ("title", "overview_copy", "program", "type", "tag")

class DataTaskAdmin(ModelAdmin):
    model = DataTask
    menu_label = "Data Task"
    menu_icon = "doc-empty"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "description", "program")
    search_fields = ("title", "description", "program", "type", "tag")

class MiniLessonAdmin(ModelAdmin):
    model = MiniLesson
    menu_label = "Mini Lesson"
    menu_icon = "doc-empty"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "description", "program")
    search_fields = ("title", "description", "program", "type", "tag")

class TakeActionAdmin(ModelAdmin):
    model = TakeAction
    menu_label = "Take Action"
    menu_icon = "doc-empty"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "description", "program")
    search_fields = ("title", "description", "program", "type", "tag")

@modeladmin_register
class ActivityAdminGroup(ModelAdminGroup):
    menu_label = "Activities"
    menu_order = 200
    items = (
        GuidedReadingAdmin,
        DataTaskAdmin,
        MiniLessonAdmin,
        TakeActionAdmin,
    )