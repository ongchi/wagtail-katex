from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    text = RichTextField(features=["katex-embed"])

    content_panels = Page.content_panels + [FieldPanel("text")]
