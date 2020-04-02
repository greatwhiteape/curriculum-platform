from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class Module(Page):
    template = "modules/module_page.html"
    ajax_template = "modules/module_page.json"

    description = RichTextField(blank=True, null=True)
    # program = SnippetChooserBlock("taxonomy.Program")
    # asset = SnippetChooserBlock("taxonomy.Assets")
    # asset_type = models.ForeignKey(
    #     'models.AssetType', 
    #     on_delete=models.SET_NULL, 
    #     null=True, 
    #     blank=True,
    #     related_name='+',
    # )    