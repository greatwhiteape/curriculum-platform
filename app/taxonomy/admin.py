from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup
)

from .models import Program, StandardsBody, Standard, Audience, Topic, AssetType, ActivityType, Tag, TimeEstimate, LearningSpace


class ProgramAdmin(ModelAdmin):
    model = Program
    menu_label = "Program"
    menu_icon = "snippet"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("program_name", "program_url")
    search_fields = ("program_name", "program_description", "program_url")


class StandardsBodyAdmin(ModelAdmin):
    model = StandardsBody
    menu_label = "Standards Bodies"
    menu_icon = "snippet"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("standards_body")
    search_fields = ("standards_body")


class StandardAdmin(ModelAdmin):
    model = Standard
    menu_label = "Standard"
    menu_icon = "snippet"
    menu_order = 310
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("standard", "standard_group", "description")
    search_fields = ("standard", "standard_group", "description")


class AudienceAdmin(ModelAdmin):
    model = Audience
    menu_label = "Audiences"
    menu_icon = "snippet"
    menu_order = 320
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("age_rage")
    search_fields = ("age_rage")


class TopicAdmin(ModelAdmin):
    model = Topic
    menu_label = "Topics"
    menu_icon = "snippet"
    menu_order = 330
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("topic")
    search_fields = ("topic")


class AssetTypeAdmin(ModelAdmin):
    model = AssetType
    menu_label = "Asset Type"
    menu_icon = "snippet"
    menu_order = 340
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("asset_type")
    search_fields = ("asset_type")


class ActivityTypeAdmin(ModelAdmin):
    model = ActivityType
    menu_label = "Type of Activity"
    menu_icon = "snippet"
    menu_order = 340
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("activity_type")
    search_fields = ("activity_type")


class TagAdmin(ModelAdmin):
    model = Tag
    menu_label = "Tags"
    menu_icon = "snippet"
    menu_order = 350
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("tag")
    search_fields = ("tag")


class TimeEstimateAdmin(ModelAdmin):
    model = TimeEstimate
    menu_label = "Time Estimates"
    menu_icon = "snippet"
    menu_order = 360
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("time_estimate")
    search_fields = ("time_estimate")

class LearningSpaceAdmin(ModelAdmin):
    model = LearningSpace
    menu_label = "Learning Spaces"
    menu_icon = "snippet"
    menu_order = 350
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("learning_space")
    search_fields = ("learning_space")


# @TODO Fix this...
# Works when linking through Snippets,
# but does not work when linking through
# TaxAdminGroup
# (seems to be missing /snippets/ in link...)
#
# @modeladmin_register
# class TaxonomyAdminGroup(ModelAdminGroup):
#     menu_label = 'Lookup Elements'
#     menu_order = 500
#     items = (
#         ActivityTypeAdmin,
#         AssetTypeAdmin,
#         AudienceAdmin,
#         ProgramAdmin,
#         StandardsBodyAdmin,
#         StandardAdmin,
#         TagAdmin,
#         TimeEstimateAdmin,
#         TopicAdmin,
#         LearningSpaceAdmin,
#     )
