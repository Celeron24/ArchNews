from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class NewArticle(Page):
    published_date = models.DateField()
    news_title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    image_url = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.CharField(max_length=50, choices=[
        ('business', 'Business'),
        ('world', 'World'),
        ('health', 'Health'),
        ('england', 'England'),
        ('asia', 'Asia'),
        ('africa', 'Africa'),
        ('entertainment', 'entertainment'),
        ('europe', 'Europe'),
        ('latinAmerica', 'LatinAmerica'),
        ('middleEast', 'MiddleEast'),
        ('northernIreland', 'NorthernIreland'),
        ('politics', 'Politics'),
        ('scotland', 'Scotland'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('usCanada', 'UsCanada'),
        ('wales', 'Wales'),
        ('general', 'General'),
    ], default='general')

    content_panels = Page.content_panels + [
        FieldPanel('published_date'),
        FieldPanel('news_title'),
        FieldPanel('description'),
        FieldPanel('link'),
        FieldPanel('image_url'),
        FieldPanel('category'),
    ]


class ContactDetail(Page):
    email = models.EmailField(null=True, blank=True),
    username = models.CharField(max_length=10, null=True, blank=True),
    phone_number = models.CharField(max_length=12, null=True, blank=True),

    content_panels = Page.content_panels + [
        FieldPanel('email'),
        FieldPanel('username'),
        FieldPanel('phone_number'),
    ]
