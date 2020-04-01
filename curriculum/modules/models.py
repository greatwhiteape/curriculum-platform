from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class Module(Page):
    template = "modules/module_page.html"

    description = RichTextField(blank=True, null=True)
    program = SnippetChooserBlock("taxonomy.Program")
    asset = SnippetChooserBlock("taxonomy.Assets")
    # asset_type = models.ForeignKey(
    #     'models.Type', 
    #     on_delete=models.SET_NULL, 
    #     null=True, 
    #     blank=True,
    #     related_name='+',
    # )    