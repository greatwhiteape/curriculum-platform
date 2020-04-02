from django.db import models

from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
# from wagtail.documents.edit_handlers import DocumentChooserPanel
# from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.snippets.edit_handlers import SnippetChooserPanel

class Asset(models.Model):
    class Meta: 
        verbose_name = "Curriculum Asset"
        verbose_name_plural = "Curriculum Assets"


    template = "assets/asset_page.html"

    title = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    program = models.ForeignKey(
        'taxonomy.Program',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )
    asset_type = models.ForeignKey(
        'taxonomy.AssetType', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )    
    student_asset = models.BooleanField(null=True)
    audience = models.ForeignKey(
        'taxonomy.Audience',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )
    tag = models.ForeignKey(
        'taxonomy.Tag', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )
    topic = models.ForeignKey(
        'taxonomy.Topic',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )


    # content_panels = Page.content_panels + [
    #     FieldPanel("description"),
    #     FieldPanel("student_asset"),
    #     SnippetChooserPanel("program"),
    #     SnippetChooserPanel("audience"),
    #     SnippetChooserPanel("asset_type"),
    #     SnippetChooserPanel("tag"),
    #     SnippetChooserPanel("topic"),
    # ]