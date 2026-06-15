from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


class ClusterableSiteSetting(BaseSiteSetting, ClusterableModel):
    """
    Combined base for settings models that need both @register_setting
    compatibility (site FK, get_permission_policy, for_site) and
    ClusterableModel (for ParentalKey / InlinePanel relationships).
    """

    class Meta:
        abstract = True
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet

from home.blocks import FooterColumnsBlock

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

    # Global color theme
    global_theme = models.ForeignKey(
        "home.ColorTheme", null=True, blank=True, default=1, on_delete=models.SET_NULL, related_name="+",
        verbose_name="Color theme",
        help_text="Select a color theme for the entire site. Color pickers are available in Snippets → Color themes.",
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

    # Button style
    BUTTON_BORDER_CHOICES = [(i, f"{i}px") for i in range(6)]
    button_border_width = models.PositiveSmallIntegerField(
        choices=BUTTON_BORDER_CHOICES,
        default=1,
        help_text="Button border width in pixels (0-5)",
    )
    button_border_color = models.CharField(
        max_length=16,
        default="#4f46e5",
        verbose_name="Button border color",
        help_text="Border color for outlined buttons",
    )
    button_padding_x = models.PositiveSmallIntegerField(
        choices=SPACING_CHOICES,
        default=24,
        verbose_name="Button horizontal padding",
    )
    button_padding_y = models.PositiveSmallIntegerField(
        choices=SPACING_CHOICES,
        default=8,
        verbose_name="Button vertical padding",
    )

    # Image overlay
    OVERLAY_OPACITY_CHOICES = [(i, f"{i}%") for i in range(0, 101, 5)]
    overlay_color = models.CharField(
        max_length=16,
        default="#ffffff",
        verbose_name="Overlay color",
        help_text="Color for the image overlay. Applied to: hero background image overlay.",
    )
    overlay_opacity = models.PositiveSmallIntegerField(
        choices=OVERLAY_OPACITY_CHOICES,
        default=75,
        verbose_name="Overlay opacity",
        help_text="Opacity percentage for the image overlay (0 = transparent, 100 = solid).",
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

    COLOR_DEFAULTS = {
        "body_text_color": "#111827",
        "heading_text_color": "#111827",
        "muted_text_color": "#667085",
        "link_color": "#4f46e5",
        "link_hover_color": "#4338ca",
        "button_primary_bg": "#4f46e5",
        "button_primary_hover": "#4338ca",
        "button_secondary_border": "#4f46e5",
        "button_secondary_hover_bg": "#4f46e5",
        "page_bg": "#ffffff",
        "surface_bg": "#f8f9fa",
        "surface_border": "#e5e7eb",
        "feature_icon_bg": "#f59e0b",
        "feature_icon_text": "#ffffff",
        "check_color": "#f59e0b",
        "brand_glow": "#4f46e5",
        "navbar_bg": "#ffffff",
        "navbar_text_color": "#111827",
        "navbar_link_color": "#667085",
        "navbar_link_hover_color": "#4f46e5",
        "footer_bg": "#f8f9fa",
        "footer_text_color": "#667085",
        "footer_heading_color": "#111827",
        "footer_link_color": "#667085",
        "footer_link_hover_color": "#4f46e5",
    }

    FIELD_TO_CSS_VAR = {
        "body_text_color": "--ks-body-text",
        "heading_text_color": "--ks-heading-text",
        "muted_text_color": "--ks-muted-text",
        "link_color": "--ks-link-text",
        "link_hover_color": "--ks-link-hover",
        "button_primary_bg": "--ks-btn-primary-bg",
        "button_primary_hover": "--ks-btn-primary-hover",
        "button_secondary_border": "--ks-btn-secondary-border",
        "button_secondary_hover_bg": "--ks-btn-secondary-hover-bg",
        "page_bg": "--ks-body-bg",
        "surface_bg": "--ks-surface-bg",
        "surface_border": "--ks-surface-border",
        "feature_icon_bg": "--ks-feature-icon-bg",
        "feature_icon_text": "--ks-feature-icon-text",
        "check_color": "--ks-check-color",
        "brand_glow": "--ks-brand-glow",
        "navbar_bg": "--ks-navbar-bg",
        "navbar_text_color": "--ks-navbar-text",
        "navbar_link_color": "--ks-navbar-link",
        "navbar_link_hover_color": "--ks-navbar-link-hover",
        "footer_bg": "--ks-footer-bg",
        "footer_text_color": "--ks-footer-text",
        "footer_heading_color": "--ks-footer-heading",
        "footer_link_color": "--ks-footer-link",
        "footer_link_hover_color": "--ks-footer-link-hover",
    }

    def resolved_colors(self):
        """Return a dict of CSS var → value, combining theme overrides with defaults."""
        theme = self.global_theme
        result = {}
        for field_name, css_var in self.FIELD_TO_CSS_VAR.items():
            if theme:
                val = getattr(theme, field_name)
                if val is not None and val != "":
                    result[css_var] = f"{val}%" if isinstance(val, int) else val
                    continue
            # Fall back to default
            dflt = self.COLOR_DEFAULTS[field_name]
            result[css_var] = f"{dflt}%" if isinstance(dflt, int) else dflt
        return result

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
                        FieldPanel("global_theme"),
                    ]
                ),
            ],
            heading="Theme selection",
            help_text="Pick a color theme for the whole site. Edit themes under Snippets → Color themes.",
            classname="ks-global-settings-group",
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
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("button_border_width"),
                        FieldPanel("button_padding_x"),
                        FieldPanel("button_padding_y"),
                    ]
                ),
            ],
            heading="Button style",
            classname="ks-global-settings-group",
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


def _color_field(verbose_name, default="", help_text=""):
    """Reusable color field — blank = inherit global."""
    return models.CharField(
        max_length=16,
        blank=True,
        default=default,
        verbose_name=verbose_name,
        help_text=help_text or f"Leave blank to inherit from global settings.",
    )


def _opacity_field():
    OPACITY_CHOICES = [(i, f"{i}%") for i in range(0, 101, 5)]
    return models.PositiveSmallIntegerField(
        choices=OPACITY_CHOICES,
        blank=True,
        null=True,
        default=None,
        verbose_name="Overlay opacity",
        help_text="Leave blank to inherit from global settings.",
    )


@register_snippet
class ColorTheme(models.Model):
    name = models.CharField(max_length=60, unique=True)
    is_default = models.BooleanField(default=False, editable=False, verbose_name="Default site theme")

    # Typography
    body_text_color = _color_field("Body text", "", "Paragraphs, copy, and general body content.")
    heading_text_color = _color_field("Heading text", "", "H1–H6 and display headings.")
    muted_text_color = _color_field("Muted text", "", "Secondary paragraphs, lead text, announcements.")

    # Links
    link_color = _color_field("Link text", "", "Text links, announcement links, eyebrow links.")
    link_hover_color = _color_field("Link hover", "", "Link text on hover.")

    # Buttons
    button_primary_bg = _color_field("Primary button", "", "Main call-to-action button background.")
    button_primary_hover = _color_field("Primary button hover", "", "Primary button on hover.")
    button_secondary_border = _color_field("Secondary button", "", "Secondary outline button border and text.")
    button_secondary_hover_bg = _color_field("Secondary button hover bg", "", "Secondary button fill on hover.")

    # Surfaces
    page_bg = _color_field("Page background", "", "Body and section background.")
    surface_bg = _color_field("Surface background", "", "Media placeholders, card fills.")
    surface_border = _color_field("Surface border", "", "Card borders, grid lines, dividers, media frames.")

    # Components
    feature_icon_bg = _color_field("Feature icon bg", "", "Feature section icon backgrounds.")
    feature_icon_text = _color_field("Feature icon text", "", "Text inside feature icons.")
    check_color = _color_field("Checklist color", "", "Checklist checkmarks.")
    brand_glow = _color_field("Brand glow", "", "Hero centered radial gradient spot.")

    # Navbar
    navbar_bg = _color_field("Navbar background", "", "Navbar bar background.")
    navbar_text_color = _color_field("Navbar text", "", "Navbar text and brand.")
    navbar_link_color = _color_field("Navbar link", "", "Navbar navigation links.")
    navbar_link_hover_color = _color_field("Navbar link hover", "", "Navbar links on hover.")

    # Footer
    footer_bg = _color_field("Footer background", "", "Footer background.")
    footer_text_color = _color_field("Footer text", "", "Footer body text.")
    footer_heading_color = _color_field("Footer heading", "", "Footer column headings.")
    footer_link_color = _color_field("Footer link", "", "Footer links.")
    footer_link_hover_color = _color_field("Footer link hover", "", "Footer links on hover.")

    panels = [
        FieldPanel("name"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("body_text_color", widget=ColorInputWidget()),
                        FieldPanel("heading_text_color", widget=ColorInputWidget()),
                        FieldPanel("muted_text_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Typography",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("link_color", widget=ColorInputWidget()),
                        FieldPanel("link_hover_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Links",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("button_primary_bg", widget=ColorInputWidget()),
                        FieldPanel("button_primary_hover", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
                FieldRowPanel(
                    [
                        FieldPanel("button_secondary_border", widget=ColorInputWidget()),
                        FieldPanel("button_secondary_hover_bg", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Buttons",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("page_bg", widget=ColorInputWidget()),
                        FieldPanel("surface_bg", widget=ColorInputWidget()),
                        FieldPanel("surface_border", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Surfaces",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("feature_icon_bg", widget=ColorInputWidget()),
                        FieldPanel("feature_icon_text", widget=ColorInputWidget()),
                        FieldPanel("check_color", widget=ColorInputWidget()),
                        FieldPanel("brand_glow", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Components",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("navbar_bg", widget=ColorInputWidget()),
                        FieldPanel("navbar_text_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
                FieldRowPanel(
                    [
                        FieldPanel("navbar_link_color", widget=ColorInputWidget()),
                        FieldPanel("navbar_link_hover_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Navbar",
            classname="ks-global-settings-group ks-global-color-group",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("footer_bg", widget=ColorInputWidget()),
                        FieldPanel("footer_text_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
                FieldRowPanel(
                    [
                        FieldPanel("footer_heading_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
                FieldRowPanel(
                    [
                        FieldPanel("footer_link_color", widget=ColorInputWidget()),
                        FieldPanel("footer_link_hover_color", widget=ColorInputWidget()),
                    ],
                    classname="ks-color-row",
                ),
            ],
            heading="Footer",
            classname="ks-global-settings-group ks-global-color-group",
        ),
    ]

    class Meta:
        verbose_name = "Color theme"
        verbose_name_plural = "Color themes"

    def __str__(self):
        label = self.name
        if self.is_default:
            label += " (Default)"
        return label


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


@register_setting
class NavbarSettings(ClusterableSiteSetting):
    logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL,
        related_name="+", verbose_name="Logo image",
        help_text="Upload a logo image. If empty, logo_text is shown as text logo.",
    )
    logo_text = models.CharField(
        max_length=120, blank=True, default="Site name",
        verbose_name="Logo text",
        help_text="Shown as text logo when no image is set.",
    )
    sticky = models.BooleanField(
        default=False, verbose_name="Sticky navbar",
        help_text="Keep the navbar fixed at the top when scrolling.",
    )
    cta_label = models.CharField(
        max_length=80, blank=True, verbose_name="CTA button label",
    )
    cta_url = models.CharField(
        max_length=255, blank=True, verbose_name="CTA button URL",
    )
    navbar_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="+", verbose_name="Navbar color theme",
    )

    FIELD_TO_CSS_VAR = {
        "navbar_bg": "--ks-navbar-bg",
        "navbar_text_color": "--ks-navbar-text",
        "navbar_link_color": "--ks-navbar-link",
        "navbar_link_hover_color": "--ks-navbar-link-hover",
    }

    @property
    def navbar_style(self):
        theme = self.navbar_theme
        if not theme:
            return ""
        parts = []
        for field_name, css_var in self.FIELD_TO_CSS_VAR.items():
            val = getattr(theme, field_name)
            if val is None or val == "":
                continue
            parts.append(f"{css_var}: {val}")
        return "; ".join(parts)

    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel("logo"),
                    FieldPanel("logo_text"),
                ]),
                FieldPanel("sticky"),
            ],
            heading="Brand & behavior",
        ),
        MultiFieldPanel(
            [
                InlinePanel("navbar_links", label="Navigation link"),
            ],
            heading="Navigation links",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel("cta_label"),
                    FieldPanel("cta_url"),
                ]),
            ],
            heading="CTA button (optional)",
        ),
        MultiFieldPanel(
            [
                FieldPanel("navbar_theme"),
            ],
            heading="Color theme",
        ),
    ]

    class Meta:
        verbose_name = "Navbar settings"
        verbose_name_plural = "Navbar settings"

    @classmethod
    def for_site(cls, site):
        return cls.objects.get_or_create(site=site)[0]


class NavbarLink(Orderable):
    settings = ParentalKey(
        NavbarSettings, related_name="navbar_links", on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=80)
    url = models.CharField(max_length=255, blank=True)

    panels = [
        FieldRowPanel([
            FieldPanel("label"),
            FieldPanel("url"),
        ]),
    ]

    def __str__(self):
        return self.label


@register_setting
class FooterSettings(ClusterableSiteSetting):
    SECTION_HEIGHT_CHOICES = [
        ("compact", "Compact"),
        ("normal", "Normal"),
        ("spacious", "Spacious"),
        ("full", "Full"),
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

    section_height = models.CharField(
        max_length=16, choices=SECTION_HEIGHT_CHOICES, default="normal",
        verbose_name="Section height",
    )
    content_width = models.CharField(
        max_length=16, choices=CONTENT_WIDTH_CHOICES, default="normal",
        verbose_name="Content width",
    )
    text_alignment = models.CharField(
        max_length=16, choices=ALIGNMENT_CHOICES, default="left",
        verbose_name="Text alignment",
    )
    vertical_alignment = models.CharField(
        max_length=16, choices=VERTICAL_ALIGNMENT_CHOICES, default="center",
        verbose_name="Vertical alignment",
    )
    anchor_id = models.CharField(
        max_length=40, blank=True, default="footer",
        verbose_name="Anchor ID",
    )
    copyright_text = models.CharField(
        max_length=255, blank=True, default="All rights reserved.",
        verbose_name="Copyright text",
    )
    bottom_bar = models.BooleanField(
        default=True, verbose_name="Show bottom bar",
        help_text="Enable the copyright bar at the bottom of the footer.",
    )
    footer_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="+", verbose_name="Footer color theme",
    )
    columns = StreamField(
        FooterColumnsBlock(), blank=True, use_json_field=True,
    )

    FIELD_TO_CSS_VAR = {
        "footer_bg": "--ks-footer-bg",
        "footer_text_color": "--ks-footer-text",
        "footer_heading_color": "--ks-footer-heading",
        "footer_link_color": "--ks-footer-link",
        "footer_link_hover_color": "--ks-footer-link-hover",
    }

    # Fallback mapping — if a footer-specific field is blank, use the theme's general equivalent
    FOOTER_FALLBACKS = {
        "footer_bg": "page_bg",
        "footer_text_color": "body_text_color",
        "footer_heading_color": "heading_text_color",
        "footer_link_color": "link_color",
        "footer_link_hover_color": "link_hover_color",
    }

    @property
    def footer_style(self):
        theme = self.footer_theme
        if not theme:
            return ""
        parts = []
        for field_name, css_var in self.FIELD_TO_CSS_VAR.items():
            val = getattr(theme, field_name)
            if val is None or val == "":
                fallback_field = self.FOOTER_FALLBACKS.get(field_name)
                if fallback_field:
                    val = getattr(theme, fallback_field, "")
            if val is None or val == "":
                continue
            parts.append(f"{css_var}: {val}")
        return "; ".join(parts)

    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel("section_height"),
                    FieldPanel("content_width"),
                ]),
                FieldRowPanel([
                    FieldPanel("text_alignment"),
                    FieldPanel("vertical_alignment"),
                ]),
                FieldPanel("anchor_id"),
            ],
            heading="Section settings",
        ),
        MultiFieldPanel(
            [
                FieldPanel("columns"),
            ],
            heading="Footer columns",
        ),
        MultiFieldPanel(
            [
                FieldPanel("copyright_text"),
                FieldPanel("bottom_bar"),
            ],
            heading="Bottom bar",
        ),
        MultiFieldPanel(
            [
                FieldPanel("footer_theme"),
            ],
            heading="Color theme",
        ),
    ]

    class Meta:
        verbose_name = "Footer settings"
        verbose_name_plural = "Footer settings"

    @classmethod
    def for_site(cls, site):
        return cls.objects.get_or_create(site=site)[0]


@register_snippet
class NavigationLinkGroup(ClusterableModel):
    name = models.CharField(max_length=80, unique=True)

    panels = [
        FieldPanel("name"),
        InlinePanel("links", label="Navigation link"),
    ]

    class Meta:
        verbose_name = "Navigation link group"
        verbose_name_plural = "Navigation link groups"
        ordering = ["name"]

    def __str__(self):
        return self.name


class NavigationLink(Orderable):
    group = ParentalKey(
        NavigationLinkGroup, related_name="links", on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=80)
    url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL,
        related_name="children",
        help_text="Parent link for nesting. Blank = top-level.",
    )

    panels = [
        FieldRowPanel([
            FieldPanel("label"),
            FieldPanel("url"),
        ]),
        FieldPanel("parent"),
    ]

    def __str__(self):
        return self.label


@register_snippet
class SocialMediaGroup(ClusterableModel):
    name = models.CharField(max_length=80, unique=True)

    panels = [
        FieldPanel("name"),
        InlinePanel("links", label="Social link"),
    ]

    class Meta:
        verbose_name = "Social media group"
        verbose_name_plural = "Social media groups"
        ordering = ["name"]

    def __str__(self):
        return self.name


class SocialLink(Orderable):
    group = ParentalKey(
        SocialMediaGroup, related_name="links", on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=80)
    url = models.CharField(max_length=255, blank=True)
    icon_class = models.CharField(
        max_length=40, blank=True,
        help_text="Bootstrap icon class (e.g., bi-twitter-x).",
    )

    panels = [
        FieldRowPanel([
            FieldPanel("label"),
            FieldPanel("url"),
            FieldPanel("icon_class"),
        ]),
    ]

    def __str__(self):
        return self.label


class HomePage(Page):
    SECTION_HEIGHT_CHOICES = [
        ("compact", "Compact"),
        ("normal", "Normal"),
        ("spacious", "Spacious"),
        ("full", "Full"),
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

    hero_enabled = models.BooleanField(default=True, verbose_name="Section enabled")
    hero_layout = models.CharField(
        max_length=40,
        choices=HERO_LAYOUT_CHOICES,
        default=HERO_CENTERED_SIMPLE,
        verbose_name="Layout",
    )
    hero_anchor_id = models.CharField(max_length=40, blank=True, default="hero", verbose_name="Anchor ID")
    hero_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
        verbose_name="Section height",
    )
    hero_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
        verbose_name="Section width",
    )
    hero_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Horizontal alignment",
    )
    hero_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Vertical alignment",
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
    hero_overlay_color = models.CharField(
        max_length=16, blank=True, default="#0f172a", verbose_name="Overlay color",
        help_text="Color tint for the background image overlay.",
    )
    OVERLAY_OPACITY_CHOICES = [(i, f"{i}%") for i in range(0, 101, 5)]
    hero_overlay_opacity = models.PositiveSmallIntegerField(
        choices=OVERLAY_OPACITY_CHOICES, blank=True, null=True, default=70,
        verbose_name="Overlay opacity",
        help_text="Transparency of the overlay (0 = transparent, 100 = solid).",
    )

    clients_enabled = models.BooleanField(default=True, verbose_name="Section enabled")
    clients_layout = models.CharField(
        max_length=40,
        choices=CLIENTS_LAYOUT_CHOICES,
        default=CLIENTS_CENTERED_HEADING_ROW,
        verbose_name="Layout",
    )
    clients_anchor_id = models.CharField(max_length=40, blank=True, default="clients", verbose_name="Anchor ID")
    clients_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
        verbose_name="Section height",
    )
    clients_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
        verbose_name="Section width",
    )
    clients_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Horizontal alignment",
    )
    clients_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Vertical alignment",
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

    features_enabled = models.BooleanField(default=True, verbose_name="Section enabled")
    features_layout = models.CharField(
        max_length=40,
        choices=FEATURES_LAYOUT_CHOICES,
        default=FEATURES_LIST_MEDIA_RIGHT,
        verbose_name="Layout",
    )
    features_anchor_id = models.CharField(max_length=40, blank=True, default="features", verbose_name="Anchor ID")
    features_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
        verbose_name="Section height",
    )
    features_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
        verbose_name="Section width",
    )
    features_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="left",
        verbose_name="Horizontal alignment",
    )
    features_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Vertical alignment",
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

    cta_enabled = models.BooleanField(default=True, verbose_name="Section enabled")
    cta_layout = models.CharField(
        max_length=40,
        choices=CTA_LAYOUT_CHOICES,
        default=CTA_LEFT_STACK,
        verbose_name="Layout",
    )
    cta_anchor_id = models.CharField(max_length=40, blank=True, default="cta", verbose_name="Anchor ID")
    cta_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
        verbose_name="Section height",
    )
    cta_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
        verbose_name="Section width",
    )
    cta_text_alignment = models.CharField(
        max_length=16,
        choices=ALIGNMENT_CHOICES,
        default="left",
        verbose_name="Horizontal alignment",
    )
    cta_vertical_alignment = models.CharField(
        max_length=16,
        choices=VERTICAL_ALIGNMENT_CHOICES,
        default="center",
        verbose_name="Vertical alignment",
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

    # Color theme overrides per section
    hero_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, default=1, on_delete=models.SET_NULL, related_name="+",
        verbose_name="Hero color theme",
    )
    clients_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, default=1, on_delete=models.SET_NULL, related_name="+",
        verbose_name="Clients color theme",
    )
    features_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, default=1, on_delete=models.SET_NULL, related_name="+",
        verbose_name="Features color theme",
    )
    cta_theme = models.ForeignKey(
        ColorTheme, null=True, blank=True, default=1, on_delete=models.SET_NULL, related_name="+",
        verbose_name="CTA color theme",
    )

    FIELD_TO_CSS_VAR = {
        "body_text_color": "--ks-body-text",
        "heading_text_color": "--ks-heading-text",
        "muted_text_color": "--ks-muted-text",
        "link_color": "--ks-link-text",
        "link_hover_color": "--ks-link-hover",
        "button_primary_bg": "--ks-btn-primary-bg",
        "button_primary_hover": "--ks-btn-primary-hover",
        "button_secondary_border": "--ks-btn-secondary-border",
        "button_secondary_hover_bg": "--ks-btn-secondary-hover-bg",
        "page_bg": "--ks-body-bg",
        "surface_bg": "--ks-surface-bg",
        "surface_border": "--ks-surface-border",
        "feature_icon_bg": "--ks-feature-icon-bg",
        "feature_icon_text": "--ks-feature-icon-text",
        "check_color": "--ks-check-color",
        "brand_glow": "--ks-brand-glow",
    }

    @staticmethod
    def _theme_style(theme):
        if not theme:
            return ""
        parts = []
        for field_name, css_var in HomePage.FIELD_TO_CSS_VAR.items():
            val = getattr(theme, field_name)
            if val is None or val == "":
                continue
            if isinstance(val, int):
                parts.append(f"{css_var}: {val}%")
            else:
                parts.append(f"{css_var}: {val}")
        return "; ".join(parts)

    @property
    def hero_style(self):
        return self._theme_style(self.hero_theme)

    @property
    def clients_style(self):
        return self._theme_style(self.clients_theme)

    @property
    def features_style(self):
        return self._theme_style(self.features_theme)

    @property
    def cta_style(self):
        return self._theme_style(self.cta_theme)

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
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("hero_overlay_color", widget=ColorInputWidget()),
                                FieldPanel("hero_overlay_opacity"),
                            ]
                        ),
                    ],
                    heading="Image overlay",
                    help_text="Color and transparency for the background image overlay (only visible on 'Background media' layout).",
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
    def _settings_panel(cls, prefix, heading, theme_field):
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
                FieldRowPanel(
                    [
                        FieldPanel(theme_field),
                    ],
                    heading="Color theme",
                ),
            ],
            heading=heading,
            classname="ks-section-settings",
        )

    section_settings_panels = [
        _settings_panel.__func__(None, "hero", "Hero settings", "hero_theme"),
        _settings_panel.__func__(None, "clients", "Client settings", "clients_theme"),
        _settings_panel.__func__(None, "features", "Feature settings", "features_theme"),
        _settings_panel.__func__(None, "cta", "CTA settings", "cta_theme"),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.pk:
            # Only populate dummy content when no explicit section data is provided
            has_content = any(kwargs.get(f) for f in [
                "hero_title", "clients_title", "features_title", "cta_title",
            ])
            if not has_content:
                self._populate_dummy_content()

    def _populate_dummy_content(self):
        self.hero_announcement = "Announcing our next product update"
        self.hero_announcement_link_label = "Read more"
        self.hero_announcement_link_url = "#"
        self.hero_title = "Build a better digital experience"
        self.hero_description = (
            "Create clear, maintainable websites with fixed sections, flexible "
            "layouts, and an editor your team can understand."
        )
        self.hero_primary_button_label = "Get started"
        self.hero_primary_button_url = "#"
        self.hero_secondary_button_label = "Learn more"
        self.hero_secondary_button_url = "#"

        self.clients_title = "Trusted by innovative teams"
        self.clients_description = (
            "A reusable client section with several layout options."
        )
        self.clients_cta_text = "Join teams building clearer digital products."
        self.clients_cta_label = "Read customer stories"
        self.clients_cta_url = "#"
        self.clients_primary_button_label = "Create account"
        self.clients_primary_button_url = "#"
        self.clients_secondary_button_label = "Contact us"
        self.clients_secondary_button_url = "#"

        self.features_eyebrow = "Deploy faster"
        self.features_title = "Everything you need to build with confidence"
        self.features_description = (
            "Choose a feature layout that matches the components your story needs."
        )
        self.features_button_label = "Get started"
        self.features_button_url = "#"
        self.features_testimonial_quote = (
            "The fixed-section editor gives our team flexibility without losing structure."
        )
        self.features_testimonial_name = "Maria Hill"
        self.features_testimonial_role = "Product Manager"

        self.cta_eyebrow = "Start today"
        self.cta_title = "Ready to build your next Wagtail website?"
        self.cta_description = (
            "Use global design settings and section layouts to move quickly."
        )
        self.cta_primary_button_label = "Get started"
        self.cta_primary_button_url = "/admin/"
        self.cta_secondary_button_label = "View features"
        self.cta_secondary_button_url = "#"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            self._populate_dummy_content()
        super().save(*args, **kwargs)
        if is_new:
            self._create_dummy_related()

    def _create_dummy_related(self):
        if not self.client_logos.exists():
            for name in ["Transistor", "Reform", "Tuple", "SavvyCal", "Statamic", "Laravel"]:
                HomeClientLogo.objects.create(page=self, name=name)

        if not self.features.exists():
            feature_data = [
                ("PD", "Push to deploy", "Publish confidently with a clear workflow."),
                ("SC", "SSL certificates", "Keep every environment protected."),
                ("SQ", "Simple queues", "Run background work without extra complexity."),
                ("AS", "Advanced security", "Apply practical controls across the platform."),
                ("API", "Powerful API", "Connect the tools your business already uses."),
                ("DB", "Database backups", "Protect important data with reliable backups."),
            ]
            for icon, title, description in feature_data:
                HomeFeature.objects.create(
                    page=self,
                    icon=icon,
                    title=title,
                    description=description,
                    link_label="Learn more",
                    link_url="#cta",
                )
