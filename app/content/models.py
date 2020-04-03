from django.db import models

from wagtail.core.models import Page

class FlexPage(Page):
    class Meta:
        verbose_name = "Misc content page"
        verbose_name_plural = "Misc content pages"

