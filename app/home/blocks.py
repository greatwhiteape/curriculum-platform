from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from modules.models import Module
from activity.models import Activity
from assets.models import Asset

class hpQuoteBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text="Block Title"
  )

  copy = blocks.CharBlock(
    required=True,
    help_text="Quote Text"
  )

  # url = blocks.U

  class Meta:
    template = "streams/hp_quoteCard_block.html"
    icon = "edit"
    label = "Grey Static Block"
    help_text = "Add static block"


class hpModuleBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text="Block Title"
  )

  image = ImageChooserBlock(
    required=True,
    help_text="Featured Block Image"
  )

  copy = blocks.CharBlock(
    required=True,
    help_text="Module Description"
  )

  module = SnippetChooserBlock(
    Module,
    required=True,
    help_text="Select Module to link to"
  )

  class Meta:
    template = "streams/hp_moduleCard_block.html"
    icon = "edit"
    label = "Module Chooser Block"
    help_text = "Add module to home page 'Featured' section"




class hpActivityBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text="Block Title"
  )

  image = ImageChooserBlock(
    required=True,
    help_text="Featured Block Image"
  )

  copy = blocks.CharBlock(
    required=True,
    help_text="Activity Description"
  )

  activity = SnippetChooserBlock(
    Activity,
    required=True,
    help_text="Select Activity to link to"
  )

  class Meta:
    template = "streams/hp_activityCard_block.html"
    icon = "edit"
    label = "Activity Chooser Block"
    help_text = "Add activity to home page 'Featured' section"




class hpAssetBlock(blocks.StructBlock):
  title = blocks.CharBlock(
    required=True,
    help_text="Block Title"
  )

  image = ImageChooserBlock(
    required=True,
    help_text="Featured Block Image"
  )

  copy = blocks.CharBlock(
    required=True,
    help_text="Asset Description"
  )

  asset = SnippetChooserBlock(
    Asset,
    required=True,
    help_text="Select Asset to link to"
  )

  class Meta:
    template = "streams/hp_assetCard_block.html"
    icon = "edit"
    label = "Asset Chooser Block"
    help_text = "Add asset to home page 'Featured' section"




# class hpFeaturedBlock(blocks.StreamBlock):
#   element = hpChooserBlock()
#   quote = hpQuoteBlock()

#   class Meta:
#     icon='cogs'

