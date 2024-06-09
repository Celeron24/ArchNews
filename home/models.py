from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail.models import Page


class HomePage(Page):
    templates = 'home/home_page.html'
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    max_count = 1
    banner_subtitle = RichTextField(features=['italic', 'bold'], blank=True, null=True)
    banner_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'

    )
    banner_cta = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]

    class Meta:
        verbose_name = "Home Page"
