from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Program, StandardsBody, Standards, Audience, Topic, Type, Tag, TimeEstimate

@modeladmin_register
class ProgramAdmin(ModelAdmin):
    model = Program
    menu_label = "Program"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("program_name", "program_description", "program_url")
    search_fields = ("program_name", "program_description", "program_url")
    
@modeladmin_register
class StandardsBodyAdmin(ModelAdmin):
    model = StandardsBody
    menu_label = "Standards Bodies"
    menu_icon = "placeholder"
    menu_order = 300
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("standards_body")
    search_fields = ("standards_body")

@modeladmin_register
class StandardsAdmin(ModelAdmin):
    model = Standards
    menu_label = "Standards"
    menu_icon = "placeholder"
    menu_order = 310
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("standard", "standard_group", "description")
    search_fields = ("standard", "standard_group", "description")
    
@modeladmin_register
class AudienceAdmin(ModelAdmin):
    model = Audience
    menu_label = "Audiences"
    menu_icon = "placeholder"
    menu_order = 320
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("age_rage")
    search_fields = ("age_rage")

@modeladmin_register
class TopicAdmin(ModelAdmin):
    model = Topic
    menu_label = "Topics"
    menu_icon = "placeholder"
    menu_order = 330
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("topic")
    search_fields = ("topic")

@modeladmin_register
class TypeAdmin(ModelAdmin):
    model = Type
    menu_label = "Types"
    menu_icon = "placeholder"
    menu_order = 340
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("type")
    search_fields = ("type")

@modeladmin_register
class TagAdmin(ModelAdmin):
    model = Tag
    menu_label = "Tags"
    menu_icon = "placeholder"
    menu_order = 350
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("tag")
    search_fields = ("tag")

@modeladmin_register
class TimeEstimateAdmin(ModelAdmin):
    model = TimeEstimate
    menu_label = "Time Estimates"
    menu_icon = "placeholder"
    menu_order = 360
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("time_estimate")
    search_fields = ("time_estimate")