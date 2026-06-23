# Wagtail Section Snippets

Use these snippets as starting points. Rename apps, paths, and field names to match the project.

## Global Design Settings

```python
# core/models.py or settings/models.py
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class DesignSystemSettings(BaseSiteSetting):
    heading_font = models.CharField(max_length=120, default="Poppins")
    body_font = models.CharField(max_length=120, default="Nunito")
    font_scale = models.CharField(
        max_length=16,
        choices=[
            ("compact", "Compact"),
            ("normal", "Normal"),
            ("large", "Large"),
        ],
        default="normal",
    )
    brand_color = models.CharField(max_length=16, default="#4f46e5")
    background_color = models.CharField(max_length=16, default="#ffffff")
    text_color = models.CharField(max_length=16, default="#111827")
    muted_text_color = models.CharField(max_length=16, default="#6b7280")
    section_padding = models.CharField(
        max_length=16,
        choices=[
            ("compact", "Compact"),
            ("normal", "Normal"),
            ("large", "Large"),
        ],
        default="normal",
    )
    container_width = models.CharField(
        max_length=16,
        choices=[
            ("narrow", "Narrow"),
            ("normal", "Normal"),
            ("wide", "Wide"),
        ],
        default="normal",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("heading_font"),
                FieldPanel("body_font"),
                FieldPanel("font_scale"),
            ],
            heading="Fonts",
        ),
        MultiFieldPanel(
            [
                FieldPanel("brand_color"),
                FieldPanel("background_color"),
                FieldPanel("text_color"),
                FieldPanel("muted_text_color"),
            ],
            heading="Colors",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_padding"),
                FieldPanel("container_width"),
            ],
            heading="Spacing",
        ),
    ]
```

```django
{# templates/base.html #}
{% load wagtailsettings_tags %}
{% get_settings %}
<style>
  :root {
    --font-heading: "{{ settings.core.DesignSystemSettings.heading_font }}", system-ui, sans-serif;
    --font-body: "{{ settings.core.DesignSystemSettings.body_font }}", system-ui, sans-serif;
    --color-brand: {{ settings.core.DesignSystemSettings.brand_color }};
    --color-bg: {{ settings.core.DesignSystemSettings.background_color }};
    --color-text: {{ settings.core.DesignSystemSettings.text_color }};
    --color-muted: {{ settings.core.DesignSystemSettings.muted_text_color }};
  }
</style>
```

## Fixed Section Page Model

```python
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


class HomeFeature(Orderable):
    page = ParentalKey("home.HomePage", related_name="features", on_delete=models.CASCADE)
    eyebrow = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_alt = models.CharField(max_length=120, blank=True)

    panels = [
        FieldRowPanel([FieldPanel("eyebrow"), FieldPanel("title")]),
        FieldPanel("description"),
        FieldRowPanel([FieldPanel("image"), FieldPanel("image_alt")]),
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
    TEXT_ALIGNMENT_CHOICES = [
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ]

    HERO_LAYOUT_CENTERED = "centered"
    HERO_LAYOUT_SPLIT_MEDIA = "split_media"
    HERO_LAYOUT_MEDIA_LEFT = "media_left"
    HERO_LAYOUT_CHOICES = [
        (HERO_LAYOUT_CENTERED, "Centered"),
        (HERO_LAYOUT_SPLIT_MEDIA, "Split media"),
        (HERO_LAYOUT_MEDIA_LEFT, "Media left"),
    ]
    HERO_VARIANTS = {
        HERO_LAYOUT_CENTERED: {
            "template": "home/includes/heroes/centered.html",
            "components": ["content", "buttons"],
            "fields": ["hero_title", "hero_description", "hero_primary_button_label"],
        },
        HERO_LAYOUT_SPLIT_MEDIA: {
            "template": "home/includes/heroes/split_media.html",
            "components": ["content", "buttons", "image"],
            "fields": [
                "hero_title",
                "hero_description",
                "hero_image",
                "hero_primary_button_label",
            ],
        },
        HERO_LAYOUT_MEDIA_LEFT: {
            "template": "home/includes/heroes/media_left.html",
            "components": ["image", "content", "buttons"],
            "fields": [
                "hero_image",
                "hero_title",
                "hero_description",
                "hero_primary_button_label",
            ],
        },
    }

    hero_enabled = models.BooleanField(
        default=True,
        verbose_name="Enable hero section",
        help_text="Show or hide the hero section without deleting its content.",
    )
    hero_layout = models.CharField(
        max_length=32,
        choices=HERO_LAYOUT_CHOICES,
        default=HERO_LAYOUT_CENTERED,
    )
    hero_anchor_id = models.CharField(max_length=32, blank=True, default="hero")
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

    @property
    def hero_template_name(self):
        return self.HERO_VARIANTS.get(
            self.hero_layout,
            self.HERO_VARIANTS[self.HERO_LAYOUT_CENTERED],
        )["template"]

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
                        FieldRowPanel([FieldPanel("hero_image"), FieldPanel("hero_image_alt")]),
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
                InlinePanel("features", label="Feature"),
            ],
            heading="Hero section",
        ),
    ]

    section_settings_panels = [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_enabled"),
                        FieldPanel("hero_layout"),
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
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(section_settings_panels, heading="Section settings"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings"),
        ]
    )
```

## Template Dispatch

```django
{# templates/home/home_page.html #}
{% extends "base.html" %}

{% block content %}
<main>
  {% if page.hero_enabled %}
    {% include page.hero_template_name %}
  {% endif %}
</main>
{% endblock %}
```

```django
{# templates/home/includes/heroes/split_media.html #}
<section id="{{ page.hero_anchor_id|default:'hero' }}" class="section section-hero section-hero-split">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        {% if page.hero_eyebrow %}<p class="eyebrow">{{ page.hero_eyebrow }}</p>{% endif %}
        <h1>{{ page.hero_title }}</h1>
        {% if page.hero_description %}<p>{{ page.hero_description|linebreaksbr }}</p>{% endif %}
        {% include "home/includes/heroes/buttons.html" %}
      </div>
      <div class="col-lg-6">
        {% if page.hero_image %}
          <img src="{{ page.hero_image.url }}" alt="{{ page.hero_image_alt|default:page.hero_title }}">
        {% else %}
          <div class="image-placeholder">Image placeholder</div>
        {% endif %}
      </div>
    </div>
  </div>
</section>
```

## Admin CSS Hook

```python
# home/wagtail_hooks.py
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("admin/css/builder-editor.css?v=section-builder-1"),
    )
```

## Admin UI CSS

```css
/* static/admin/css/builder-editor.css */
.ks-editor-group[data-ks-panel] {
  margin-block: 1rem;
  padding: 1rem;
  border: 1px solid #d8dee8;
  border-radius: 0.5rem;
  background: #fff;
}

.ks-editor-section-settings[data-ks-panel] {
  border-color: #b8d5ff;
  background: #eef6ff;
}

.ks-editor-subgroup[data-ks-panel] {
  margin-block: 1rem;
  padding: 1rem;
  border: 1px dashed #c8d2df;
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.7);
}

.ks-editor-settings-grid .w-panel__content,
.ks-editor-settings-grid .w-field-row {
  display: grid;
  grid-template-columns: repeat(2, minmax(220px, 1fr));
  gap: 1rem;
}

.ks-editor-settings-grid .w-field {
  margin-bottom: 0;
}

.ks-editor-settings-grid input,
.ks-editor-settings-grid select {
  max-width: 22rem;
}

@media (max-width: 800px) {
  .ks-editor-settings-grid .w-panel__content,
  .ks-editor-settings-grid .w-field-row {
    grid-template-columns: 1fr;
  }
}
```

## Testing Checklist

```python
def test_section_layout_can_change(self):
    self.homepage.hero_layout = HomePage.HERO_LAYOUT_SPLIT_MEDIA
    self.homepage.save(update_fields=["hero_layout"])
    response = self.client.get(self.homepage.url)
    self.assertContains(response, "section-hero-split")


def test_section_can_be_disabled(self):
    self.homepage.hero_enabled = False
    self.homepage.save(update_fields=["hero_enabled"])
    response = self.client.get(self.homepage.url)
    self.assertNotContains(response, 'id="hero"')


def test_section_settings_are_available_in_editor(self):
    edit_handler = HomePage.get_edit_handler()
    form_class = edit_handler.get_form_class()
    self.assertIn("hero_layout", form_class.base_fields)
    self.assertIn("hero_section_height", form_class.base_fields)
```

