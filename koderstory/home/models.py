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
from wagtail.models import Orderable, Page


class HomeClientLogo(Orderable):
    page = ParentalKey(
        "home.HomePage",
        related_name="client_logos",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=80)

    panels = [FieldPanel("name")]


class HomeCardBase(Orderable):
    eyebrow = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_alt = models.CharField(max_length=120, blank=True)
    button_label = models.CharField(max_length=80, blank=True)
    button_url = models.CharField(max_length=255, blank=True)

    panels = [
        FieldRowPanel(
            [
                FieldPanel("eyebrow"),
                FieldPanel("title"),
            ]
        ),
        FieldPanel("description"),
        FieldRowPanel(
            [
                FieldPanel("image"),
                FieldPanel("image_alt"),
            ]
        ),
        FieldRowPanel(
            [
                FieldPanel("button_label"),
                FieldPanel("button_url"),
            ]
        ),
    ]

    class Meta:
        abstract = True


class HomeServiceCard(HomeCardBase):
    page = ParentalKey(
        "home.HomePage",
        related_name="service_cards",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["sort_order"]


class HomeProductCard(HomeCardBase):
    page = ParentalKey(
        "home.HomePage",
        related_name="product_cards",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["sort_order"]


class HomePage(Page):
    IMAGE_POSITION_CHOICES = [
        ("left", "Left"),
        ("right", "Right"),
    ]
    HEADING_CATEGORY_CHOICES = [
        ("heading_1", "Heading 1"),
        ("heading_2", "Heading 2"),
        ("heading_3", "Heading 3"),
    ]
    TEXT_FONT_SIZE_CHOICES = [
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]
    BUTTON_STYLE_CHOICES = [
        ("primary", "Primary"),
        ("secondary", "Secondary"),
        ("outline", "Outline"),
    ]
    ANIMATION_CHOICES = [
        ("none", "None"),
        ("fade_in", "Fade in"),
        ("slide_up", "Slide up"),
    ]
    SECTION_HEIGHT_CHOICES = [
        ("compact", "Compact"),
        ("normal", "Normal"),
        ("large", "Large"),
    ]
    CONTENT_WIDTH_CHOICES = [
        ("narrow", "Narrow"),
        ("normal", "Normal"),
        ("large", "Large"),
        ("full", "Full width"),
    ]
    TEXT_ALIGNMENT_CHOICES = [
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ]
    CONTENT_VERTICAL_ALIGNMENT_CHOICES = [
        ("top", "Top"),
        ("center", "Center"),
        ("bottom", "Bottom"),
    ]
    CONTENT_HORIZONTAL_ALIGNMENT_CHOICES = [
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ]

    HERO_LAYOUT_CENTERED_SIMPLE = "centered_simple"
    HERO_LAYOUT_CENTERED_PREVIEW = "centered_preview"
    HERO_LAYOUT_SPLIT_IMAGE_RIGHT = "split_image_right"
    HERO_LAYOUT_ANGLED_IMAGE_RIGHT = "angled_image_right"
    HERO_LAYOUT_CHOICES = [
        (HERO_LAYOUT_CENTERED_SIMPLE, "Centered simple"),
        (HERO_LAYOUT_CENTERED_PREVIEW, "Centered with preview image"),
        (HERO_LAYOUT_SPLIT_IMAGE_RIGHT, "Split image right"),
        (HERO_LAYOUT_ANGLED_IMAGE_RIGHT, "Angled image right"),
    ]

    CLIENTS_LAYOUT_CARD_SPLIT = "card_split"
    CLIENTS_LAYOUT_HEADING_TOP = "heading_top"
    CLIENTS_LAYOUT_CTA_BOTTOM = "cta_bottom"
    CLIENTS_LAYOUT_SPLIT_GRID = "split_grid"
    CLIENTS_LAYOUT_SIMPLE_ROW = "simple_row"
    CLIENTS_LAYOUT_DARK_GRID = "dark_grid"
    CLIENTS_LAYOUT_DARK_ROW = "dark_row"
    CLIENTS_LAYOUT_CHOICES = [
        (CLIENTS_LAYOUT_CARD_SPLIT, "Card split"),
        (CLIENTS_LAYOUT_HEADING_TOP, "Heading top"),
        (CLIENTS_LAYOUT_CTA_BOTTOM, "CTA bottom"),
        (CLIENTS_LAYOUT_SPLIT_GRID, "Split grid"),
        (CLIENTS_LAYOUT_SIMPLE_ROW, "Simple row"),
        (CLIENTS_LAYOUT_DARK_GRID, "Dark grid"),
        (CLIENTS_LAYOUT_DARK_ROW, "Dark row"),
    ]

    SERVICES_LAYOUT_CARD_GRID = "card_grid"
    SERVICES_LAYOUT_MEDIA_RIGHT = "media_right"
    SERVICES_LAYOUT_CENTERED_GRID = "centered_grid"
    SERVICES_LAYOUT_DARK_MEDIA = "dark_media"
    SERVICES_LAYOUT_MEDIA_TOP = "media_top"
    SERVICES_LAYOUT_MEDIA_LEFT = "media_left"
    SERVICES_LAYOUT_SIMPLE_COLUMNS = "simple_columns"
    SERVICES_LAYOUT_CHECKLIST = "checklist"
    SERVICES_LAYOUT_DARK_GRID = "dark_grid"
    SERVICES_LAYOUT_CHOICES = [
        (SERVICES_LAYOUT_CARD_GRID, "Card grid"),
        (SERVICES_LAYOUT_MEDIA_RIGHT, "Media right"),
        (SERVICES_LAYOUT_CENTERED_GRID, "Centered grid"),
        (SERVICES_LAYOUT_DARK_MEDIA, "Dark media"),
        (SERVICES_LAYOUT_MEDIA_TOP, "Media top"),
        (SERVICES_LAYOUT_MEDIA_LEFT, "Media left"),
        (SERVICES_LAYOUT_SIMPLE_COLUMNS, "Simple columns"),
        (SERVICES_LAYOUT_CHECKLIST, "Checklist"),
        (SERVICES_LAYOUT_DARK_GRID, "Dark grid"),
    ]

    CTA_LAYOUT_SPLIT = "split"
    CTA_LAYOUT_LEFT_STACK = "left_stack"
    CTA_LAYOUT_CENTERED = "centered"
    CTA_LAYOUT_DARK_CENTERED = "dark_centered"
    CTA_LAYOUT_GRADIENT_CENTERED = "gradient_centered"
    CTA_LAYOUT_BAR = "bar"
    CTA_LAYOUT_SPLIT_MEDIA = "split_media"
    CTA_LAYOUT_MEDIA_LEFT = "media_left"
    CTA_LAYOUT_BENEFIT_GRID = "benefit_grid"
    CTA_LAYOUT_CHOICES = [
        (CTA_LAYOUT_SPLIT, "Split"),
        (CTA_LAYOUT_LEFT_STACK, "Left stack"),
        (CTA_LAYOUT_CENTERED, "Centered"),
        (CTA_LAYOUT_DARK_CENTERED, "Dark centered"),
        (CTA_LAYOUT_GRADIENT_CENTERED, "Gradient centered"),
        (CTA_LAYOUT_BAR, "Bar"),
        (CTA_LAYOUT_SPLIT_MEDIA, "Split media"),
        (CTA_LAYOUT_MEDIA_LEFT, "Media left"),
        (CTA_LAYOUT_BENEFIT_GRID, "Benefit grid"),
    ]

    hero_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable hero section",
        help_text="Show or hide the hero section without deleting its content.",
    )
    hero_anchor_id = models.CharField(max_length=32, blank=True, default="hero")
    hero_layout = models.CharField(
        max_length=40,
        choices=HERO_LAYOUT_CHOICES,
        default=HERO_LAYOUT_SPLIT_IMAGE_RIGHT,
        help_text="Choose how the hero content and image are arranged.",
    )
    hero_image_position = models.CharField(
        max_length=16,
        choices=IMAGE_POSITION_CHOICES,
        default="right",
    )
    hero_heading_category = models.CharField(
        max_length=16,
        choices=HEADING_CATEGORY_CHOICES,
        default="heading_1",
    )
    hero_text_font_size = models.CharField(
        max_length=16,
        choices=TEXT_FONT_SIZE_CHOICES,
        default="medium",
    )
    hero_button_style = models.CharField(
        max_length=16,
        choices=BUTTON_STYLE_CHOICES,
        default="primary",
    )
    hero_animation = models.CharField(
        max_length=16,
        choices=ANIMATION_CHOICES,
        default="none",
    )
    hero_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
    )
    hero_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    hero_text_alignment = models.CharField(
        max_length=16,
        choices=TEXT_ALIGNMENT_CHOICES,
        default="left",
    )
    hero_content_vertical_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    hero_content_horizontal_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_HORIZONTAL_ALIGNMENT_CHOICES,
        default="left",
    )
    hero_eyebrow = models.CharField(max_length=80, blank=True)
    hero_title = models.CharField(max_length=180, blank=True)
    hero_description = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_image_alt = models.CharField(max_length=120, blank=True)
    hero_buttons_enabled = models.BooleanField(
        default=False,
        verbose_name="Enable hero buttons",
        help_text="Show or hide the hero call-to-action buttons.",
    )
    hero_primary_button_label = models.CharField(max_length=80, blank=True)
    hero_primary_button_url = models.CharField(max_length=255, blank=True)
    hero_secondary_button_label = models.CharField(max_length=80, blank=True)
    hero_secondary_button_url = models.CharField(max_length=255, blank=True)

    clients_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable client logo section",
        help_text="Show or hide the client logo section without deleting its content.",
    )
    clients_anchor_id = models.CharField(max_length=32, blank=True, default="clients")
    clients_layout = models.CharField(
        max_length=32,
        choices=CLIENTS_LAYOUT_CHOICES,
        default=CLIENTS_LAYOUT_CARD_SPLIT,
        help_text="Choose the visual layout for client logos.",
    )
    clients_heading_category = models.CharField(
        max_length=16,
        choices=HEADING_CATEGORY_CHOICES,
        default="heading_2",
    )
    clients_text_font_size = models.CharField(
        max_length=16,
        choices=TEXT_FONT_SIZE_CHOICES,
        default="medium",
    )
    clients_animation = models.CharField(
        max_length=16,
        choices=ANIMATION_CHOICES,
        default="none",
    )
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
        choices=TEXT_ALIGNMENT_CHOICES,
        default="left",
    )
    clients_content_vertical_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    clients_content_horizontal_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_HORIZONTAL_ALIGNMENT_CHOICES,
        default="left",
    )
    clients_eyebrow = models.CharField(max_length=80, blank=True)
    clients_title = models.CharField(max_length=180, blank=True)

    services_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable services section",
        help_text="Show or hide the services section without deleting its content.",
    )
    services_anchor_id = models.CharField(max_length=32, blank=True, default="services")
    services_layout = models.CharField(
        max_length=32,
        choices=SERVICES_LAYOUT_CHOICES,
        default=SERVICES_LAYOUT_CARD_GRID,
        help_text="Choose the visual layout for service cards.",
    )
    services_heading_category = models.CharField(
        max_length=16,
        choices=HEADING_CATEGORY_CHOICES,
        default="heading_2",
    )
    services_text_font_size = models.CharField(
        max_length=16,
        choices=TEXT_FONT_SIZE_CHOICES,
        default="medium",
    )
    services_button_style = models.CharField(
        max_length=16,
        choices=BUTTON_STYLE_CHOICES,
        default="primary",
    )
    services_animation = models.CharField(
        max_length=16,
        choices=ANIMATION_CHOICES,
        default="none",
    )
    services_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
    )
    services_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    services_text_alignment = models.CharField(
        max_length=16,
        choices=TEXT_ALIGNMENT_CHOICES,
        default="left",
    )
    services_content_vertical_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    services_content_horizontal_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_HORIZONTAL_ALIGNMENT_CHOICES,
        default="left",
    )
    services_kicker = models.CharField(max_length=80, blank=True)
    services_title = models.CharField(max_length=180, blank=True)
    services_description = models.TextField(blank=True)
    services_button_label = models.CharField(max_length=80, blank=True)
    services_button_url = models.CharField(max_length=255, blank=True)

    products_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable products section",
        help_text="Show or hide the products section without deleting its content.",
    )
    products_anchor_id = models.CharField(max_length=32, blank=True, default="products")
    products_heading_category = models.CharField(
        max_length=16,
        choices=HEADING_CATEGORY_CHOICES,
        default="heading_2",
    )
    products_text_font_size = models.CharField(
        max_length=16,
        choices=TEXT_FONT_SIZE_CHOICES,
        default="medium",
    )
    products_button_style = models.CharField(
        max_length=16,
        choices=BUTTON_STYLE_CHOICES,
        default="primary",
    )
    products_animation = models.CharField(
        max_length=16,
        choices=ANIMATION_CHOICES,
        default="none",
    )
    products_section_height = models.CharField(
        max_length=16,
        choices=SECTION_HEIGHT_CHOICES,
        default="normal",
    )
    products_content_width = models.CharField(
        max_length=16,
        choices=CONTENT_WIDTH_CHOICES,
        default="normal",
    )
    products_text_alignment = models.CharField(
        max_length=16,
        choices=TEXT_ALIGNMENT_CHOICES,
        default="left",
    )
    products_content_vertical_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    products_content_horizontal_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_HORIZONTAL_ALIGNMENT_CHOICES,
        default="left",
    )
    products_kicker = models.CharField(max_length=80, blank=True)
    products_title = models.CharField(max_length=180, blank=True)
    products_description = models.TextField(blank=True)
    products_button_label = models.CharField(max_length=80, blank=True)
    products_button_url = models.CharField(max_length=255, blank=True)

    cta_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable CTA section",
        help_text="Show or hide the CTA section without deleting its content.",
    )
    cta_anchor_id = models.CharField(max_length=32, blank=True, default="cta")
    cta_layout = models.CharField(
        max_length=32,
        choices=CTA_LAYOUT_CHOICES,
        default=CTA_LAYOUT_SPLIT,
        help_text="Choose the visual layout for the CTA section.",
    )
    cta_heading_category = models.CharField(
        max_length=16,
        choices=HEADING_CATEGORY_CHOICES,
        default="heading_2",
    )
    cta_text_font_size = models.CharField(
        max_length=16,
        choices=TEXT_FONT_SIZE_CHOICES,
        default="medium",
    )
    cta_button_style = models.CharField(
        max_length=16,
        choices=BUTTON_STYLE_CHOICES,
        default="primary",
    )
    cta_animation = models.CharField(
        max_length=16,
        choices=ANIMATION_CHOICES,
        default="none",
    )
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
        choices=TEXT_ALIGNMENT_CHOICES,
        default="left",
    )
    cta_content_vertical_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_VERTICAL_ALIGNMENT_CHOICES,
        default="center",
    )
    cta_content_horizontal_alignment = models.CharField(
        max_length=16,
        choices=CONTENT_HORIZONTAL_ALIGNMENT_CHOICES,
        default="left",
    )
    cta_kicker = models.CharField(max_length=80, blank=True)
    cta_title = models.CharField(max_length=180, blank=True)
    cta_description = models.TextField(blank=True)
    cta_primary_button_label = models.CharField(max_length=80, blank=True)
    cta_primary_button_url = models.CharField(max_length=255, blank=True)
    cta_secondary_button_label = models.CharField(max_length=80, blank=True)
    cta_secondary_button_url = models.CharField(max_length=255, blank=True)

    @property
    def hero_template_name(self):
        template_names = {
            self.HERO_LAYOUT_CENTERED_SIMPLE: "home/includes/heroes/centered_simple.html",
            self.HERO_LAYOUT_CENTERED_PREVIEW: "home/includes/heroes/centered_preview.html",
            self.HERO_LAYOUT_SPLIT_IMAGE_RIGHT: "home/includes/heroes/split_image_right.html",
            self.HERO_LAYOUT_ANGLED_IMAGE_RIGHT: "home/includes/heroes/angled_image_right.html",
        }
        return template_names.get(
            self.hero_layout,
            "home/includes/heroes/split_image_right.html",
        )

    @property
    def clients_template_name(self):
        template_names = {
            self.CLIENTS_LAYOUT_CARD_SPLIT: "home/includes/clients/card_split.html",
            self.CLIENTS_LAYOUT_HEADING_TOP: "home/includes/clients/heading_top.html",
            self.CLIENTS_LAYOUT_CTA_BOTTOM: "home/includes/clients/cta_bottom.html",
            self.CLIENTS_LAYOUT_SPLIT_GRID: "home/includes/clients/split_grid.html",
            self.CLIENTS_LAYOUT_SIMPLE_ROW: "home/includes/clients/simple_row.html",
            self.CLIENTS_LAYOUT_DARK_GRID: "home/includes/clients/dark_grid.html",
            self.CLIENTS_LAYOUT_DARK_ROW: "home/includes/clients/dark_row.html",
        }
        return template_names.get(
            self.clients_layout,
            "home/includes/clients/card_split.html",
        )

    @property
    def services_template_name(self):
        template_names = {
            self.SERVICES_LAYOUT_CARD_GRID: "home/includes/services/card_grid.html",
            self.SERVICES_LAYOUT_MEDIA_RIGHT: "home/includes/services/media_right.html",
            self.SERVICES_LAYOUT_CENTERED_GRID: "home/includes/services/centered_grid.html",
            self.SERVICES_LAYOUT_DARK_MEDIA: "home/includes/services/dark_media.html",
            self.SERVICES_LAYOUT_MEDIA_TOP: "home/includes/services/media_top.html",
            self.SERVICES_LAYOUT_MEDIA_LEFT: "home/includes/services/media_left.html",
            self.SERVICES_LAYOUT_SIMPLE_COLUMNS: "home/includes/services/simple_columns.html",
            self.SERVICES_LAYOUT_CHECKLIST: "home/includes/services/checklist.html",
            self.SERVICES_LAYOUT_DARK_GRID: "home/includes/services/dark_grid.html",
        }
        return template_names.get(
            self.services_layout,
            "home/includes/services/card_grid.html",
        )

    @property
    def cta_template_name(self):
        template_names = {
            self.CTA_LAYOUT_SPLIT: "home/includes/ctas/split.html",
            self.CTA_LAYOUT_LEFT_STACK: "home/includes/ctas/left_stack.html",
            self.CTA_LAYOUT_CENTERED: "home/includes/ctas/centered.html",
            self.CTA_LAYOUT_DARK_CENTERED: "home/includes/ctas/dark_centered.html",
            self.CTA_LAYOUT_GRADIENT_CENTERED: "home/includes/ctas/gradient_centered.html",
            self.CTA_LAYOUT_BAR: "home/includes/ctas/bar.html",
            self.CTA_LAYOUT_SPLIT_MEDIA: "home/includes/ctas/split_media.html",
            self.CTA_LAYOUT_MEDIA_LEFT: "home/includes/ctas/media_left.html",
            self.CTA_LAYOUT_BENEFIT_GRID: "home/includes/ctas/benefit_grid.html",
        }
        return template_names.get(
            self.cta_layout,
            "home/includes/ctas/split.html",
        )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_eyebrow"),
                        FieldPanel("hero_title"),
                        FieldPanel("hero_description"),
                    ],
                    heading="Hero content",
                    classname="ks-editor-group ks-editor-group-content",
                    attrs={"data-ks-panel": "hero-content"},
                ),
                MultiFieldPanel(
                    [
                        FieldRowPanel(
                            [
                                FieldPanel("hero_image"),
                                FieldPanel("hero_image_alt"),
                            ]
                        ),
                    ],
                    heading="Hero media",
                    classname="ks-editor-group ks-editor-group-media",
                    attrs={"data-ks-panel": "hero-media"},
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
                    heading="Hero buttons",
                    classname="ks-editor-group ks-editor-group-buttons",
                    attrs={"data-ks-panel": "hero-buttons"},
                ),
            ],
            heading="Hero section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("clients_eyebrow"),
                FieldPanel("clients_title"),
                InlinePanel("client_logos", label="Client"),
            ],
            heading="Client logo section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("services_kicker"),
                FieldPanel("services_title"),
                FieldPanel("services_description"),
                FieldRowPanel(
                    [
                        FieldPanel("services_button_label"),
                        FieldPanel("services_button_url"),
                    ]
                ),
                InlinePanel("service_cards", label="Service card"),
            ],
            heading="Services section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("products_kicker"),
                FieldPanel("products_title"),
                FieldPanel("products_description"),
                FieldRowPanel(
                    [
                        FieldPanel("products_button_label"),
                        FieldPanel("products_button_url"),
                    ]
                ),
                InlinePanel("product_cards", label="Product card"),
            ],
            heading="Products section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("cta_kicker"),
                FieldPanel("cta_title"),
                FieldPanel("cta_description"),
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
            heading="CTA section",
        ),
    ]

    section_settings_panels = [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_enabled"),
                        FieldPanel("hero_layout"),
                        FieldPanel("hero_buttons_enabled"),
                        FieldPanel("hero_image_position"),
                        FieldPanel("hero_heading_category"),
                        FieldPanel("hero_text_font_size"),
                        FieldPanel("hero_button_style"),
                        FieldPanel("hero_animation"),
                    ],
                    heading="Settings",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "hero-settings-basic"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_anchor_id"),
                        FieldPanel("hero_section_height"),
                        FieldPanel("hero_content_width"),
                        FieldPanel("hero_text_alignment"),
                        FieldPanel("hero_content_vertical_alignment"),
                        FieldPanel("hero_content_horizontal_alignment"),
                    ],
                    heading="Advanced",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "hero-settings-advanced"},
                ),
            ],
            heading="Hero settings",
            classname="ks-editor-group ks-editor-section-settings",
            attrs={"data-ks-panel": "hero-settings"},
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("clients_enabled"),
                        FieldPanel("clients_layout"),
                        FieldPanel("clients_heading_category"),
                        FieldPanel("clients_text_font_size"),
                        FieldPanel("clients_animation"),
                    ],
                    heading="Settings",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "clients-settings-basic"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("clients_anchor_id"),
                        FieldPanel("clients_section_height"),
                        FieldPanel("clients_content_width"),
                        FieldPanel("clients_text_alignment"),
                        FieldPanel("clients_content_vertical_alignment"),
                        FieldPanel("clients_content_horizontal_alignment"),
                    ],
                    heading="Advanced",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "clients-settings-advanced"},
                ),
            ],
            heading="Client logo settings",
            classname="ks-editor-group ks-editor-group-settings",
            attrs={"data-ks-panel": "clients-settings"},
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("services_enabled"),
                        FieldPanel("services_layout"),
                        FieldPanel("services_heading_category"),
                        FieldPanel("services_text_font_size"),
                        FieldPanel("services_button_style"),
                        FieldPanel("services_animation"),
                    ],
                    heading="Settings",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "services-settings-basic"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("services_anchor_id"),
                        FieldPanel("services_section_height"),
                        FieldPanel("services_content_width"),
                        FieldPanel("services_text_alignment"),
                        FieldPanel("services_content_vertical_alignment"),
                        FieldPanel("services_content_horizontal_alignment"),
                    ],
                    heading="Advanced",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "services-settings-advanced"},
                ),
            ],
            heading="Services settings",
            classname="ks-editor-group ks-editor-group-settings",
            attrs={"data-ks-panel": "services-settings"},
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("products_enabled"),
                        FieldPanel("products_heading_category"),
                        FieldPanel("products_text_font_size"),
                        FieldPanel("products_button_style"),
                        FieldPanel("products_animation"),
                    ],
                    heading="Settings",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "products-settings-basic"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("products_anchor_id"),
                        FieldPanel("products_section_height"),
                        FieldPanel("products_content_width"),
                        FieldPanel("products_text_alignment"),
                        FieldPanel("products_content_vertical_alignment"),
                        FieldPanel("products_content_horizontal_alignment"),
                    ],
                    heading="Advanced",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "products-settings-advanced"},
                ),
            ],
            heading="Products settings",
            classname="ks-editor-group ks-editor-group-settings",
            attrs={"data-ks-panel": "products-settings"},
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("cta_enabled"),
                        FieldPanel("cta_layout"),
                        FieldPanel("cta_heading_category"),
                        FieldPanel("cta_text_font_size"),
                        FieldPanel("cta_button_style"),
                        FieldPanel("cta_animation"),
                    ],
                    heading="Settings",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "cta-settings-basic"},
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("cta_anchor_id"),
                        FieldPanel("cta_section_height"),
                        FieldPanel("cta_content_width"),
                        FieldPanel("cta_text_alignment"),
                        FieldPanel("cta_content_vertical_alignment"),
                        FieldPanel("cta_content_horizontal_alignment"),
                    ],
                    heading="Advanced",
                    classname="ks-editor-subgroup ks-editor-settings-grid",
                    attrs={"data-ks-panel": "cta-settings-advanced"},
                ),
            ],
            heading="CTA settings",
            classname="ks-editor-group ks-editor-group-settings",
            attrs={"data-ks-panel": "cta-settings"},
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(section_settings_panels, heading="Section settings"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings"),
        ]
    )
