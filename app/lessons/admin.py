from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Lesson

@modeladmin_register
class LessonAdmin(ModelAdmin):
    model = Lesson
    menu_label = "Lesson"
    menu_icon = "form"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "program", "live")
    search_fields = ("title", "overview_copy", "learning_outcomes")
