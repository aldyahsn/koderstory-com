from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
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
    hero_anchor_id = models.CharField(max_length=32, blank=True, default="hero")
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
    hero_primary_button_label = models.CharField(max_length=80, blank=True)
    hero_primary_button_url = models.CharField(max_length=255, blank=True)
    hero_secondary_button_label = models.CharField(max_length=80, blank=True)
    hero_secondary_button_url = models.CharField(max_length=255, blank=True)

    clients_anchor_id = models.CharField(max_length=32, blank=True, default="clients")
    clients_eyebrow = models.CharField(max_length=80, blank=True)
    clients_title = models.CharField(max_length=180, blank=True)

    services_anchor_id = models.CharField(max_length=32, blank=True, default="services")
    services_kicker = models.CharField(max_length=80, blank=True)
    services_title = models.CharField(max_length=180, blank=True)
    services_description = models.TextField(blank=True)
    services_button_label = models.CharField(max_length=80, blank=True)
    services_button_url = models.CharField(max_length=255, blank=True)

    products_anchor_id = models.CharField(max_length=32, blank=True, default="products")
    products_kicker = models.CharField(max_length=80, blank=True)
    products_title = models.CharField(max_length=180, blank=True)
    products_description = models.TextField(blank=True)
    products_button_label = models.CharField(max_length=80, blank=True)
    products_button_url = models.CharField(max_length=255, blank=True)

    cta_anchor_id = models.CharField(max_length=32, blank=True, default="cta")
    cta_kicker = models.CharField(max_length=80, blank=True)
    cta_title = models.CharField(max_length=180, blank=True)
    cta_description = models.TextField(blank=True)
    cta_primary_button_label = models.CharField(max_length=80, blank=True)
    cta_primary_button_url = models.CharField(max_length=255, blank=True)
    cta_secondary_button_label = models.CharField(max_length=80, blank=True)
    cta_secondary_button_url = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_anchor_id"),
                FieldPanel("hero_eyebrow"),
                FieldPanel("hero_title"),
                FieldPanel("hero_description"),
                FieldRowPanel(
                    [
                        FieldPanel("hero_image"),
                        FieldPanel("hero_image_alt"),
                    ]
                ),
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
            heading="Hero section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("clients_anchor_id"),
                FieldPanel("clients_eyebrow"),
                FieldPanel("clients_title"),
                InlinePanel("client_logos", label="Client"),
            ],
            heading="Client logo section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("services_anchor_id"),
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
                FieldPanel("products_anchor_id"),
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
                FieldPanel("cta_anchor_id"),
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
