from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

class TitleBlock(blocks.StructBlock):
  text = blocks.CharBlock(
    required=True,
    help_text='Text to display',
  )

  class Meta:
    template = "streams/title_block.html"
    icon = "edit"
    label = "Title"
    help_text = "Centered text to display on the page"

class Link(blocks.StructBlock):
  link_text = blocks.CharBlock(
    max_length=50,
    default='Asset can be accessed here.'
  )

  url = blocks.URLBlock(
    required=True,
    help_text="Link to external resource"
  )

  class Meta:
    template = "streams/link_block.html"
    icon = "edit"
    label = "Link"
    help_text = "Link to external resource"

class GoogleDocEmbed(blocks.StructBlock):
  url = blocks.URLBlock(
    required=True,
    help_text="Link to Google Doc"
  )

  class Meta:
    template = "streams/gd_embed_block.html"
    icon = "edit"
    label = "Google Doc"
    help_text = "Embed a Google Doc"

class CODAPEmbed(blocks.StructBlock):
  url = blocks.URLBlock(
    required=True,
    help_text="Link to CODAP"
  )

  class Meta:
    template = "streams/CODAP_embed_block.html"
    icon = "edit"
    label = "CODAP"
    help_text = "Embed a CODAP exercise"


class ChapterBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text='Chapter Title',
  )
  body = blocks.RichTextBlock(
    required=False,
    help_text='Chapter Description',
  )

  class Meta:
    template = "streams/chapter_block.html"
    icon = "edit"
    label = "Chapter Block"
    help_text = "Chapter Description"



class LessonBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text='Chapter Title',
  )
  body = blocks.RichTextBlock(
    required=True,
    help_text='Chapter Description',
  )

  class Meta:
    template = "streams/chapter_block.html"
    icon = "edit"
    label = "Chapter Block"
    help_text = "Chapter Description"

class YouTubeBlock(blocks.StructBlock):
  youtube_video = blocks.CharBlock(
    required=True,
    help_text='YouTube Video ID (https://youtu.be/XXX-XXX the XXX-XXX section)',
  )

  class Meta:
    template = "streams/video_block.html"
    icon = "media"
    label = "Embed YouTube Video"



# class LinkValue(blocks.StructValue):

#     def url(self) -> str:
#         internal_page = self.get("internal_page")
#         external_link = self.get("external_link")
#         if internal_page:
#             return internal_page.url
#         elif external_link:
#             return external_link
#         return ""

# class Link(blocks.StructBlock):
#     link_text = blocks.CharBlock(
#         max_length=50,
#         default='More Details'
#     )
#     internal_page = blocks.PageChooserBlock(
#         required=False
#     )
#     external_link = blocks.URLBlock(
#         required=False
#     )

#     class Meta:
#         value_class = LinkValue

#     def clean(self, value):
#         internal_page = value.get("internal_page")
#         external_link = value.get("external_link")
#         errors = {}
#         if internal_page and external_link:
#             errors["internal_page"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
#             errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
#         elif not internal_page and not external_link:
#             errors["internal_page"] = ErrorList(["Please select a page or enter a URL for one of these options."])
#             errors["external_link"] = ErrorList(["Please select a page or enter a URL for one of these options."])

#         if errors:
#             raise ValidationError("Validation error in your Link", params=errors)

        # return super().clean(value)
