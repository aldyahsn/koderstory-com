from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField

from home.widgets import ColorInputWidget

RICH_TEXT_FEATURES = [
    "bold",
    "italic",
    "link",
    "ol",
    "ul",
    "h3",
    "h4",
    "align-left",
    "align-center",
    "align-right",
]
from wagtail.models import Orderable, Page


@register_setting
class DesignSystemSettings(BaseSiteSetting):
    # Google Fonts choices
    FONT_CHOICES = [
        ("Inter", "Inter"),
        ("Roboto", "Roboto"),
        ("Open Sans", "Open Sans"),
        ("Lato", "Lato"),
        ("Montserrat", "Montserrat"),
        ("Poppins", "Poppins"),
        ("Nunito", "Nunito"),
        ("Playfair Display", "Playfair Display"),
        ("Merriweather", "Merriweather"),
        ("Source Sans Pro", "Source Sans Pro"),
    ]

    # Font size choices
    FONT_SIZE_CHOICES = [
        (14, "14px"),
        (16, "16px (Default)"),
        (18, "18px"),
        (20, "20px"),
    ]

    # Line height choices
    LINE_HEIGHT_CHOICES = [
        (1.2, "1.2 (Tight)"),
        (1.4, "1.4"),
        (1.5, "1.5 (Default)"),
        (1.6, "1.6"),
        (1.8, "1.8 (Relaxed)"),
    ]

    # Letter spacing choices
    LETTER_SPACING_CHOICES = [
        ("normal", "Normal"),
        ("-1px", "-1px (Tight)"),
        ("-0.5px", "-0.5px"),
        ("0.5px", "0.5px"),
        ("1px", "1px (Wide)"),
        ("2px", "2px"),
    ]

    # Spacing scale choices
    SPACING_CHOICES = [
        (4, "4px (XS)"),
        (8, "8px (SM)"),
        (16, "16px (MD)"),
        (24, "24px"),
        (32, "32px (LG)"),
        (48, "48px (XL)"),
        (64, "64px (2XL)"),
    ]

    # Typography
    heading_font = models.CharField(
        max_length=120,
        choices=FONT_CHOICES,
        default="Poppins",
    )
    body_font = models.CharField(
        max_length=120,
        choices=FONT_CHOICES,
        default="Nunito",
    )
    base_font_size = models.PositiveSmallIntegerField(
        choices=FONT_SIZE_CHOICES,
        default=16,
    )
    line_height = models.FloatField(
        choices=LINE_HEIGHT_CHOICES,
        default=1.5,
    )
    letter_spacing = models.CharField(
        max_length=10,
        choices=LETTER_SPACING_CHOICES,
        default="normal",
    )

    # Heading sizes (in rem units based on base font size)
    h1_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=3.0,
        help_text="H1 size in rem (e.g., 3.0 = 3rem = 48px with 16px base)",
    )
    h2_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=2.5,
        help_text="H2 size in rem",
    )
    h3_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=2.0,
        help_text="H3 size in rem",
    )
    h4_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.5,
        help_text="H4 size in rem",
    )
    h5_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.25,
        help_text="H5 size in rem",
    )
    h6_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.0,
        help_text="H6 size in rem",
    )

    # Theme Colors
    brand_color = models.CharField(max_length=16, default="#4f46e5", verbose_name="Brand")
    primary_color = models.CharField(
        max_length=16,
        default="#3b82f6",
        verbose_name="Primary",
        help_text="Primary action color",
    )
    secondary_color = models.CharField(
        max_length=16,
        default="#8b5cf6",
        verbose_name="Secondary",
        help_text="Secondary accent color",
    )
    accent_color = models.CharField(
        max_length=16,
        default="#f59e0b",
        verbose_name="Accent",
        help_text="Accent/highlight color",
    )

    # Semantic Colors
    success_color = models.CharField(max_length=16, default="#10b981", verbose_name="Success")
    warning_color = models.CharField(max_length=16, default="#f59e0b", verbose_name="Warning")
    error_color = models.CharField(max_length=16, default="#ef4444", verbose_name="Error")
    info_color = models.CharField(max_length=16, default="#3b82f6", verbose_name="Info")

    # Surface Colors
    background_color = models.CharField(max_length=16, default="#ffffff", verbose_name="Background")
    surface_color = models.CharField(max_length=16, default="#f8f9fa", verbose_name="Surface")
    surface_variant_color = models.CharField(
        max_length=16,
        default="#e5e7eb",
        verbose_name="Surface variant",
        help_text="Secondary surface color",
    )

    # Text Colors
    text_color = models.CharField(max_length=16, default="#111827", verbose_name="Text")
    text_muted_color = models.CharField(max_length=16, default="#667085", verbose_name="Muted")
    text_on_brand_color = models.CharField(
        max_length=16,
        default="#ffffff",
        verbose_name="On brand",
        help_text="Text color on brand/primary backgrounds",
    )

    # Spacing Scale
    spacing_xs = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=4)
    spacing_sm = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=8)
    spacing_md = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=16)
    spacing_lg = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=32)
    spacing_xl = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=48)
    spacing_2xl = models.PositiveSmallIntegerField(choices=SPACING_CHOICES, default=64)

    # Layout
    section_padding = models.PositiveSmallIntegerField(
        default=80,
        help_text="Default vertical section padding in pixels.",
    )
    container_width = models.PositiveSmallIntegerField(
        default=1200,
        help_text="Maximum content width in pixels.",
    )

    # Border Radius
    button_radius = models.PositiveSmallIntegerField(default=6)
    card_radius = models.PositiveSmallIntegerField(default=12)
    input_radius = models.PositiveSmallIntegerField(
        default=6,
        help_text="Form inputs border radius",
    )

    @property
    def google_fonts_url(self):
        """Generate Google Fonts URL based on selected heading and body fonts."""
        return (
            f"https://fonts.googleapis.com/css2?"
            f"family={self.heading_font}:wght@500;600&"
            f"family={self.body_font}:wght@400;600&"
            f"display=swap"
        )

    typography_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("heading_font"),
                        FieldPanel("body_font"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("base_font_size"),
                        FieldPanel("line_height"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("letter_spacing"),
                    ]
                ),
            ],
            heading="Font family and base",
            classname="ks-global-settings-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("h1_size"),
                        FieldPanel("h2_size"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("h3_size"),
                        FieldPanel("h4_size"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("h5_size"),
                        FieldPanel("h6_size"),
                    ]
                ),
            ],
            heading="Heading scale",
            classname="ks-global-settings-group",
        ),
    ]

    color_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("brand_color", widget=ColorInputWidget()),
                        FieldPanel("primary_color", widget=ColorInputWidget()),
                        FieldPanel("secondary_color", widget=ColorInputWidget()),
                        FieldPanel("accent_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Brand colors",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("success_color", widget=ColorInputWidget()),
                        FieldPanel("warning_color", widget=ColorInputWidget()),
                        FieldPanel("error_color", widget=ColorInputWidget()),
                        FieldPanel("info_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Status colors",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("background_color", widget=ColorInputWidget()),
                        FieldPanel("surface_color", widget=ColorInputWidget()),
                        FieldPanel("surface_variant_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Surface colors",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("text_color", widget=ColorInputWidget()),
                        FieldPanel("text_muted_color", widget=ColorInputWidget()),
                        FieldPanel("text_on_brand_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Text colors",
            classname="ks-global-settings-group ks-global-color-group",
        ),
    ]

    layout_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("spacing_xs"),
                        FieldPanel("spacing_sm"),
                        FieldPanel("spacing_md"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("spacing_lg"),
                        FieldPanel("spacing_xl"),
                        FieldPanel("spacing_2xl"),
                    ]
                ),
            ],
            heading="Spacing scale",
            classname="ks-global-settings-group ks-global-settings-group--three",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("section_padding"),
                        FieldPanel("container_width"),
                    ]
                ),
            ],
            heading="Page layout",
            classname="ks-global-settings-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("button_radius"),
                        FieldPanel("card_radius"),
                        FieldPanel("input_radius"),
                    ]
                ),
            ],
            heading="Corner radius",
            classname="ks-global-settings-group ks-global-settings-group--three",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(typography_panels, heading="Typography"),
            ObjectList(color_panels, heading="Colors"),
            ObjectList(layout_panels, heading="Layout & components"),
        ]
    )

    class Meta:
        verbose_name = "Global settings"
        verbose_name_plural = "Global settings"


class HomeClientLogo(Orderable):
    page = ParentalKey(
        "home.HomePage",
        related_name="client_logos",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=80)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    url = models.CharField(max_length=255, blank=True)

    panels = [
        FieldRowPanel([FieldPanel("name"), FieldPanel("url")]),
        FieldPanel("logo"),
    ]


class HomeFeature(Orderable):
    page = ParentalKey(
        "home.HomePage",
        related_name="features",
        on_delete=models.CASCADE,
    )
    icon = models.CharField(
        max_length=32,
        blank=True,
        help_text="Short icon name or initials.",
    )
    title = models.CharField(max_length=120)
    description = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    link_label = models.CharField(max_length=80, blank=True)
    link_url = models.CharField(max_length=255, blank=True)

    panels = [
        FieldRowPanel([FieldPanel("icon"), FieldPanel("title")]),
        FieldPanel("description"),
        FieldRowPanel([FieldPanel("link_label"), FieldPanel("link_url")]),
    ]


class HomePage(Page):
    SECTION_HEIGHT_CHOICES = [
        ("compact", "Compact"),
        ("normal", "Normal"),
        ("large", "Large"),
    ]
    CONTENT_WIDTH_CHOICES = [
        ("narrow", "Narrow"),
        ("normal", "Normal"),
        ("wide", "Wide"),
        ("full", "Full width"),
    ]
    ALIGNMENT_CHOICES = [
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ]
    VERTICAL_ALIGNMENT_CHOICES = [
        ("top", "Top"),
        ("center", "Center"),
        ("bottom", "Bottom"),
    ]

    HERO_CENTERED_SIMPLE = "centered_simple"
    HERO_SPLIT_MEDIA_RIGHT = "split_media_right"
    HERO_BACKGROUND_MEDIA = "background_media"
    HERO_CENTERED_MEDIA_BELOW = "centered_media_below"
    HERO_HALF_MEDIA_RIGHT = "half_media_right"
    HERO_ANGLED_MEDIA_RIGHT = "angled_media_right"
    HERO_VARIANTS = {
        HERO_CENTERED_SIMPLE: {
            "label": "Centered simple",
            "template": "home/sections/hero/centered_simple.html",
            "components": ["announcement", "copy", "buttons"],
        },
        HERO_SPLIT_MEDIA_RIGHT: {
            "label": "Split media right",
            "template": "home/sections/hero/split_media_right.html",
            "components": ["announcement", "copy", "buttons", "media"],
        },
        HERO_BACKGROUND_MEDIA: {
            "label": "Background media",
            "template": "home/sections/hero/background_media.html",
            "components": ["announcement", "copy", "buttons", "media"],
        },
        HERO_CENTERED_MEDIA_BELOW: {
            "label": "Centered with media below",
            "template": "home/sections/hero/centered_media_below.html",
            "components": ["copy", "buttons", "media"],
        },
        HERO_HALF_MEDIA_RIGHT: {
            "label": "Half media right",
            "template": "home/sections/hero/half_media_right.html",
            "components": ["announcement", "copy", "buttons", "media"],
        },
        HERO_ANGLED_MEDIA_RIGHT: {
            "label": "Angled media right",
            "template": "home/sections/hero/angled_media_right.html",
            "components": ["announcement", "copy", "buttons", "media"],
        },
    }
    HERO_LAYOUT_CHOICES = [
        (key, value["label"]) for key, value in HERO_VARIANTS.items()
    ]

    CLIENTS_CENTERED_HEADING_ROW = "centered_heading_row"
    CLIENTS_ROW_CTA = "row_cta"
    CLIENTS_LEFT_HEADING_ROW = "left_heading_row"
    CLIENTS_SPLIT_COPY_GRID = "split_copy_grid"
    CLIENTS_BORDERED_GRID = "bordered_grid"
    CLIENTS_VARIANTS = {
        CLIENTS_CENTERED_HEADING_ROW: {
            "label": "Centered heading with logo row",
            "template": "home/sections/clients/centered_heading_row.html",
            "components": ["copy", "logos"],
        },
        CLIENTS_ROW_CTA: {
            "label": "Logo row with CTA",
            "template": "home/sections/clients/row_cta.html",
            "components": ["logos", "cta"],
        },
        CLIENTS_LEFT_HEADING_ROW: {
            "label": "Left heading with logo row",
            "template": "home/sections/clients/left_heading_row.html",
            "components": ["copy", "logos"],
        },
        CLIENTS_SPLIT_COPY_GRID: {
            "label": "Split copy with logo grid",
            "template": "home/sections/clients/split_copy_grid.html",
            "components": ["copy", "logos", "buttons"],
        },
        CLIENTS_BORDERED_GRID: {
            "label": "Bordered logo grid",
            "template": "home/sections/clients/bordered_grid.html",
            "components": ["logos"],
        },
    }
    CLIENTS_LAYOUT_CHOICES = [
        (key, value["label"]) for key, value in CLIENTS_VARIANTS.items()
    ]

    FEATURES_LIST_MEDIA_RIGHT = "list_media_right"
    FEATURES_CENTERED_TWO_COLUMN = "centered_two_column"
    FEATURES_MEDIA_GRID = "media_grid"
    FEATURES_HEADING_MEDIA_BELOW = "heading_media_below"
    FEATURES_CENTERED_THREE_COLUMN = "centered_three_column"
    FEATURES_MEDIA_LEFT_LIST = "media_left_list"
    FEATURES_CARD_COLUMNS = "card_columns"
    FEATURES_SPLIT_MEDIA_LIST = "split_media_list"
    FEATURES_SPLIT_MEDIA_TESTIMONIAL = "split_media_testimonial"
    FEATURES_HEADING_LEFT_GRID = "heading_left_grid"
    FEATURES_INTRO_CHECKLIST = "intro_checklist"
    FEATURES_FEATURE_GRID = "feature_grid"
    FEATURES_VARIANTS = {
        FEATURES_LIST_MEDIA_RIGHT: {
            "label": "Feature list with media right",
            "template": "home/sections/features/list_media_right.html",
            "components": ["copy", "items", "media"],
        },
        FEATURES_CENTERED_TWO_COLUMN: {
            "label": "Centered two-column grid",
            "template": "home/sections/features/centered_two_column.html",
            "components": ["copy", "items"],
        },
        FEATURES_MEDIA_GRID: {
            "label": "Media with feature grid",
            "template": "home/sections/features/media_grid.html",
            "components": ["copy", "media", "items"],
        },
        FEATURES_HEADING_MEDIA_BELOW: {
            "label": "Heading with media below",
            "template": "home/sections/features/heading_media_below.html",
            "components": ["copy", "media"],
        },
        FEATURES_CENTERED_THREE_COLUMN: {
            "label": "Centered three-column grid",
            "template": "home/sections/features/centered_three_column.html",
            "components": ["copy", "items"],
        },
        FEATURES_MEDIA_LEFT_LIST: {
            "label": "Media left with feature list",
            "template": "home/sections/features/media_left_list.html",
            "components": ["copy", "media", "items"],
        },
        FEATURES_CARD_COLUMNS: {
            "label": "Three-column feature cards",
            "template": "home/sections/features/card_columns.html",
            "components": ["copy", "items"],
        },
        FEATURES_SPLIT_MEDIA_LIST: {
            "label": "Split media with feature list",
            "template": "home/sections/features/split_media_list.html",
            "components": ["copy", "media", "items", "button"],
        },
        FEATURES_SPLIT_MEDIA_TESTIMONIAL: {
            "label": "Split media with testimonial",
            "template": "home/sections/features/split_media_testimonial.html",
            "components": ["copy", "media", "button", "testimonial"],
        },
        FEATURES_HEADING_LEFT_GRID: {
            "label": "Heading left with feature grid",
            "template": "home/sections/features/heading_left_grid.html",
            "components": ["copy", "items"],
        },
        FEATURES_INTRO_CHECKLIST: {
            "label": "Intro with checklist grid",
            "template": "home/sections/features/intro_checklist.html",
            "components": ["copy", "items"],
        },
        FEATURES_FEATURE_GRID: {
            "label": "Feature grid",
            "template": "home/sections/features/feature_grid.html",
            "components": ["copy", "items"],
        },
    }
    FEATURES_LAYOUT_CHOICES = [
        (key, value["label"]) for key, value in FEATURES_VARIANTS.items()
    ]

    CTA_LEFT_STACK = "left_stack"
    CTA_CENTERED = "centered"
    CTA_HORIZONTAL_SPLIT = "horizontal_split"
    CTA_MEDIA_LEFT = "media_left"
    CTA_VARIANTS = {
        CTA_LEFT_STACK: {
            "label": "Left stacked",
            "template": "home/sections/cta/left_stack.html",
            "components": ["copy", "buttons"],
        },
        CTA_CENTERED: {
            "label": "Centered",
            "template": "home/sections/cta/centered.html",
            "components": ["copy", "buttons"],
        },
        CTA_HORIZONTAL_SPLIT: {
            "label": "Horizontal split",
            "template": "home/sections/cta/horizontal_split.html",
            "components": ["copy", "buttons"],
        },
        CTA_MEDIA_LEFT: {
            "label": "Media left",
            "template": "home/sections/cta/media_left.html",
            "components": ["copy", "buttons", "media"],
        },
    }
    CTA_LAYOUT_CHOICES = [
        (key, value["label"]) for key, value in CTA_VARIANTS.items()
    ]

    hero_enabled = models.BooleanField(default=True)
    hero_layout = models.CharField(
        max_length=40,
        choices=HERO_LAYOUT_CHOICES,
        default=HERO_CENTERED_SIMPLE,
    )
    hero_anchor_id = models.CharField(max_length=40, blank=True, default="hero")
    hero_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="large",
    )
    hero_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    hero_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="center",
    )
    hero_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    hero_announcement = models.CharField(max_length=160, blank=True)
    hero_announcement_link_label = models.CharField(max_length=80, blank=True)
    hero_announcement_link_url = models.CharField(max_length=255, blank=True)
    hero_title = models.CharField(max_length=180, blank=True)
    hero_description = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    hero_primary_button_label = models.CharField(max_length=80, blank=True)
    hero_primary_button_url = models.CharField(max_length=255, blank=True)
    hero_secondary_button_label = models.CharField(max_length=80, blank=True)
    hero_secondary_button_url = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_image_alt = models.CharField(max_length=120, blank=True)

    clients_enabled = models.BooleanField(default=True)
    clients_layout = models.CharField(
        max_length=40,
        choices=CLIENTS_LAYOUT_CHOICES,
        default=CLIENTS_CENTERED_HEADING_ROW,
    )
    clients_anchor_id = models.CharField(max_length=40, blank=True, default="clients")
    clients_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
    )
    clients_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    clients_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="center",
    )
    clients_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    clients_title = models.CharField(max_length=180, blank=True)
    clients_description = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    clients_cta_text = models.CharField(max_length=180, blank=True)
    clients_cta_label = models.CharField(max_length=80, blank=True)
    clients_cta_url = models.CharField(max_length=255, blank=True)
    clients_primary_button_label = models.CharField(max_length=80, blank=True)
    clients_primary_button_url = models.CharField(max_length=255, blank=True)
    clients_secondary_button_label = models.CharField(max_length=80, blank=True)
    clients_secondary_button_url = models.CharField(max_length=255, blank=True)

    features_enabled = models.BooleanField(default=True)
    features_layout = models.CharField(
        max_length=40,
        choices=FEATURES_LAYOUT_CHOICES,
        default=FEATURES_LIST_MEDIA_RIGHT,
    )
    features_anchor_id = models.CharField(max_length=40, blank=True, default="features")
    features_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="large",
    )
    features_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    features_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="left",
    )
    features_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    features_eyebrow = models.CharField(max_length=80, blank=True)
    features_title = models.CharField(max_length=180, blank=True)
    features_description = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    features_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    features_image_alt = models.CharField(max_length=120, blank=True)
    features_button_label = models.CharField(max_length=80, blank=True)
    features_button_url = models.CharField(max_length=255, blank=True)
    features_testimonial_quote = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    features_testimonial_name = models.CharField(max_length=100, blank=True)
    features_testimonial_role = models.CharField(max_length=120, blank=True)
    features_testimonial_avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    cta_enabled = models.BooleanField(default=True)
    cta_layout = models.CharField(
        max_length=40,
        choices=CTA_LAYOUT_CHOICES,
        default=CTA_LEFT_STACK,
    )
    cta_anchor_id = models.CharField(max_length=40, blank=True, default="cta")
    cta_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
    )
    cta_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    cta_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="left",
    )
    cta_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    cta_eyebrow = models.CharField(max_length=80, blank=True)
    cta_title = models.CharField(max_length=180, blank=True)
    cta_description = RichTextField(blank=True, features=RICH_TEXT_FEATURES)
    cta_primary_button_label = models.CharField(max_length=80, blank=True)
    cta_primary_button_url = models.CharField(max_length=255, blank=True)
    cta_secondary_button_label = models.CharField(max_length=80, blank=True)
    cta_secondary_button_url = models.CharField(max_length=255, blank=True)
    cta_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cta_image_alt = models.CharField(max_length=120, blank=True)

    @staticmethod
    def _variant_template(variants, selected, fallback):
        return variants.get(selected, variants[fallback])["template"]

    @property
    def hero_template_name(self):
        return self._variant_template(
            self.HERO_VARIANTS,
            self.hero_layout,
            self.HERO_CENTERED_SIMPLE,
        )

    @property
    def clients_template_name(self):
        return self._variant_template(
            self.CLIENTS_VARIANTS,
            self.clients_layout,
            self.CLIENTS_CENTERED_HEADING_ROW,
        )

    @property
    def features_template_name(self):
        return self._variant_template(
            self.FEATURES_VARIANTS,
            self.features_layout,
            self.FEATURES_LIST_MEDIA_RIGHT,
        )

    @property
    def cta_template_name(self):
        return self._variant_template(
            self.CTA_VARIANTS,
            self.cta_layout,
            self.CTA_LEFT_STACK,
        )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_announcement"),
                        FieldRowPanel(
                            [
                                FieldPanel("hero_announcement_link_label"),
                                FieldPanel("hero_announcement_link_url"),
                            ]
                        ),
                    ],
                    heading="Announcement",
                    classname="ks-component-group",
                    attrs={
                        "data-section": "hero",
                        "data-component": "announcement",
                    },
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_title"),
                        FieldPanel("hero_description"),
                    ],
                    heading="Content",
                    classname="ks-component-group",
                    attrs={"data-section": "hero", "data-component": "copy"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("hero_primary_button_label"),
                                FieldPanel("hero_primary_button_url"),
                            ]
                        ),
                        FieldRowPanel(
                            [
                                FieldPanel("hero_secondary_button_label"),
                                FieldPanel("hero_secondary_button_url"),
                            ]
                        ),
                    ],
                    heading="Buttons",
                    classname="ks-component-group",
                    attrs={"data-section": "hero", "data-component": "buttons"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [FieldPanel("hero_image"), FieldPanel("hero_image_alt")]
                        )
                    ],
                    heading="Media",
                    classname="ks-component-group",
                    attrs={"data-section": "hero", "data-component": "media"},
                ),
            ],
            heading="Hero section",
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("clients_title"),
                        FieldPanel("clients_description"),
                    ],
                    heading="Content",
                    classname="ks-component-group",
                    attrs={"data-section": "clients", "data-component": "copy"},
                ),
                MultiFieldPanel(
                    [InlinePanel("client_logos", label="Client logo")],
                    heading="Logos",
                    classname="ks-component-group",
                    attrs={"data-section": "clients", "data-component": "logos"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("clients_cta_text"),
                        FieldRowPanel(
                            [
                                FieldPanel("clients_cta_label"),
                                FieldPanel("clients_cta_url"),
                            ]
                        ),
                    ],
                    heading="CTA message",
                    classname="ks-component-group",
                    attrs={"data-section": "clients", "data-component": "cta"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("clients_primary_button_label"),
                                FieldPanel("clients_primary_button_url"),
                            ]
                        ),
                        FieldRowPanel(
                            [
                                FieldPanel("clients_secondary_button_label"),
                                FieldPanel("clients_secondary_button_url"),
                            ]
                        ),
                    ],
                    heading="Buttons",
                    classname="ks-component-group",
                    attrs={"data-section": "clients", "data-component": "buttons"},
                ),
            ],
            heading="Client section",
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("features_eyebrow"),
                        FieldPanel("features_title"),
                        FieldPanel("features_description"),
                    ],
                    heading="Content",
                    classname="ks-component-group",
                    attrs={"data-section": "features", "data-component": "copy"},
                ),
                MultiFieldPanel(
                    [InlinePanel("features", label="Feature")],
                    heading="Feature items",
                    classname="ks-component-group",
                    attrs={"data-section": "features", "data-component": "items"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("features_image"),
                                FieldPanel("features_image_alt"),
                            ]
                        )
                    ],
                    heading="Media",
                    classname="ks-component-group",
                    attrs={"data-section": "features", "data-component": "media"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("features_button_label"),
                                FieldPanel("features_button_url"),
                            ]
                        )
                    ],
                    heading="Button",
                    classname="ks-component-group",
                    attrs={"data-section": "features", "data-component": "button"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("features_testimonial_quote"),
                        FieldRowPanel(
                            [
                                FieldPanel("features_testimonial_name"),
                                FieldPanel("features_testimonial_role"),
                            ]
                        ),
                        FieldPanel("features_testimonial_avatar"),
                    ],
                    heading="Testimonial",
                    classname="ks-component-group",
                    attrs={
                        "data-section": "features",
                        "data-component": "testimonial",
                    },
                ),
            ],
            heading="Feature section",
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("cta_eyebrow"),
                        FieldPanel("cta_title"),
                        FieldPanel("cta_description"),
                    ],
                    heading="Content",
                    classname="ks-component-group",
                    attrs={"data-section": "cta", "data-component": "copy"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("cta_primary_button_label"),
                                FieldPanel("cta_primary_button_url"),
                            ]
                        ),
                        FieldRowPanel(
                            [
                                FieldPanel("cta_secondary_button_label"),
                                FieldPanel("cta_secondary_button_url"),
                            ]
                        ),
                    ],
                    heading="Buttons",
                    classname="ks-component-group",
                    attrs={"data-section": "cta", "data-component": "buttons"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [FieldPanel("cta_image"), FieldPanel("cta_image_alt")]
                        )
                    ],
                    heading="Media",
                    classname="ks-component-group",
                    attrs={"data-section": "cta", "data-component": "media"},
                ),
            ],
            heading="CTA section",
        ),
    ]

    @classmethod
    def _settings_panel(cls, prefix, heading):
        return MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel(f"{prefix}_enabled", classname="w-field--small"),
                        FieldPanel(f"{prefix}_layout"),
                    ],
                    heading="Layout",
                ),
                FieldRowPanel(
                    [
                        FieldPanel(f"{prefix}_section_height"),
                        FieldPanel(f"{prefix}_content_width"),
                    ],
                    heading="Spacing",
                ),
                FieldRowPanel(
                    [
                        FieldPanel(f"{prefix}_text_alignment"),
                        FieldPanel(f"{prefix}_vertical_alignment"),
                    ],
                    heading="Alignment",
                ),
                FieldRowPanel(
                    [
                        FieldPanel(f"{prefix}_anchor_id"),
                    ],
                    heading="Advanced",
                ),
            ],
            heading=heading,
            classname="ks-section-settings",
        )

    section_settings_panels = [
        _settings_panel.__func__(None, "hero", "Hero settings"),
        _settings_panel.__func__(None, "clients", "Client settings"),
        _settings_panel.__func__(None, "features", "Feature settings"),
        _settings_panel.__func__(None, "cta", "CTA settings"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(section_settings_panels, heading="Section settings"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings"),
        ]
    )

    class Meta:
        verbose_name = "Home page"
