from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from .choices import (
    BUTTON_SHAPE_CHOICES,
    FONT_CHOICES,
    IMAGE_RADIUS_CHOICES,
    IMAGE_SHADOW_CHOICES,
    PLACEHOLDER_STYLE_CHOICES,
    THEME_CHOICES,
)
from .tokens import default_color_schemes


@register_setting(icon="cog")
class SiteDesignSettings(BaseSiteSetting):
    active_theme = models.CharField(
        max_length=32,
        choices=THEME_CHOICES,
        default="minimal_saas",
    )

    primary_color = models.CharField(max_length=7, default="#4f46e5")
    accent_color = models.CharField(max_length=7, default="#ecfe3a")
    background_color = models.CharField(max_length=7, default="#ffffff")
    text_color = models.CharField(max_length=7, default="#111827")
    color_schemes = models.JSONField(default=default_color_schemes)

    heading_font = models.CharField(
        max_length=128,
        choices=FONT_CHOICES,
        default="Inter, ui-sans-serif, system-ui, sans-serif",
    )
    body_font = models.CharField(
        max_length=128,
        choices=FONT_CHOICES,
        default="Inter, ui-sans-serif, system-ui, sans-serif",
    )
    button_font = models.CharField(
        max_length=128,
        choices=FONT_CHOICES,
        default="Inter, ui-sans-serif, system-ui, sans-serif",
    )

    button_shape = models.CharField(
        max_length=16,
        choices=BUTTON_SHAPE_CHOICES,
        default="soft",
    )
    button_border_width = models.PositiveSmallIntegerField(default=1)
    button_padding = models.CharField(max_length=16, default="normal")

    image_radius = models.CharField(
        max_length=16,
        choices=IMAGE_RADIUS_CHOICES,
        default="md",
    )
    image_shadow = models.CharField(
        max_length=16,
        choices=IMAGE_SHADOW_CHOICES,
        default="soft",
    )
    placeholder_style = models.CharField(
        max_length=32,
        choices=PLACEHOLDER_STYLE_CHOICES,
        default="brand_mark",
    )
    default_hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    default_card_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    default_avatar_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    favicon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    default_og_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    cookie_banner_enabled = models.BooleanField(default=False)
    cookie_banner_text = models.CharField(
        max_length=255,
        blank=True,
        default="We use cookies to improve your experience.",
    )

    analytics_id = models.CharField(max_length=80, blank=True)
    custom_css_variables = models.TextField(
        blank=True,
        help_text="Superuser-only escape hatch. Add CSS variable declarations only.",
    )
    head_html = models.TextField(blank=True)
    footer_html = models.TextField(blank=True)

    color_panels = [
        FieldPanel("primary_color"),
        FieldPanel("accent_color"),
        FieldPanel("background_color"),
        FieldPanel("text_color"),
        FieldPanel("color_schemes"),
    ]
    font_panels = [
        FieldPanel("heading_font"),
        FieldPanel("body_font"),
        FieldPanel("button_font"),
    ]
    button_panels = [
        FieldPanel("button_shape"),
        FieldPanel("button_border_width"),
        FieldPanel("button_padding"),
    ]
    image_panels = [
        FieldPanel("image_radius"),
        FieldPanel("image_shadow"),
        FieldPanel("placeholder_style"),
        FieldPanel("default_hero_image"),
        FieldPanel("default_card_image"),
        FieldPanel("default_avatar_image"),
        FieldPanel("default_og_image"),
    ]
    meta_panels = [
        FieldPanel("favicon"),
        FieldPanel("cookie_banner_enabled"),
        FieldPanel("cookie_banner_text"),
    ]
    advanced_panels = [
        FieldPanel("active_theme"),
        FieldPanel("analytics_id"),
        FieldPanel("custom_css_variables"),
        FieldPanel("head_html"),
        FieldPanel("footer_html"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(color_panels, heading="Colors"),
            ObjectList(font_panels, heading="Fonts"),
            ObjectList(button_panels, heading="Buttons"),
            ObjectList(image_panels, heading="Images"),
            ObjectList(meta_panels, heading="Favicon & Cookies"),
            ObjectList(advanced_panels, heading="Advanced"),
        ]
    )

    class Meta:
        verbose_name = "Site design settings"
