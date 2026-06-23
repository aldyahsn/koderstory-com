from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField


@register_setting(icon="text-align-left")
class TypographySettings(BaseSiteSetting):
    h1_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H1 headings (e.g., 'Inter', 'Playfair Display')",
    )
    h2_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H2 headings (e.g., 'Inter', 'Playfair Display')",
    )
    h3_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H3 headings (e.g., 'Inter', 'Playfair Display')",
    )
    h4_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H4 headings (e.g., 'Inter', 'Playfair Display')",
    )
    h5_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H5 headings (e.g., 'Inter', 'Playfair Display')",
    )
    h6_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for H6 headings (e.g., 'Inter', 'Playfair Display')",
    )
    paragraph_font = models.CharField(
        max_length=255,
        blank=True,
        help_text="Font family for paragraph text (e.g., 'Inter', 'Open Sans')",
    )
    paragraph_font_weight = models.CharField(
        max_length=50,
        blank=True,
        help_text="Font weight for paragraph text (e.g., 'normal', '300', '400', '500', '600')",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("h1_font"),
                FieldPanel("h2_font"),
                FieldPanel("h3_font"),
                FieldPanel("h4_font"),
                FieldPanel("h5_font"),
                FieldPanel("h6_font"),
            ],
            heading="Headings (H1-H6)",
        ),
        FieldPanel("paragraph_font"),
        FieldPanel("paragraph_font_weight"),
    ]

    def __str__(self):
        return "Typography Settings"