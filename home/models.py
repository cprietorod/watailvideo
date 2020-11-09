from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.models import Document, AbstractDocument

class CustomDocument(AbstractDocument):
    # Custom field example:
    source = models.CharField(
        max_length=255,
        # This must be set to allow Wagtail to create a document instance
        # on upload.
        blank=True,
        null=True
    )

    admin_form_fields = Document.admin_form_fields + (
        # Add all custom fields names to make them appear in the form:
        'source',
    )

class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class RegularPage(Page):
    body = RichTextField(blank=True)
    book_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body',classname="full"),
        DocumentChooserPanel('book_file'),
    ]