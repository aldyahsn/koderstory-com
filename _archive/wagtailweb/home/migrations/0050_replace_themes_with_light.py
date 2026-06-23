from django.db import migrations

LIGHT_THEME_DATA = {
    "name": "Light",
    "is_default": True,
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

THEME_FK_FIELDS = [
    ("home", "DesignSystemSettings", "global_theme"),
    ("home", "HomePage", "hero_theme"),
    ("home", "HomePage", "clients_theme"),
    ("home", "HomePage", "features_theme"),
    ("home", "HomePage", "cta_theme"),
    ("home", "ServicePage", "header_theme"),
    ("home", "ServicePage", "content_theme"),
    ("home", "ServicePage", "services_theme"),
    ("home", "ServiceDetailPage", "header_theme"),
    ("home", "ServiceDetailPage", "bento_theme"),
    ("home", "ServiceDetailPage", "content_theme"),
    ("home", "ServiceDetailPage", "features_theme"),
    ("home", "ServiceDetailPage", "cta_theme"),
    ("home", "BlogIndexPage", "header_theme"),
    ("home", "BlogIndexPage", "blog_theme"),
    ("home", "BlogIndexPage", "cta_theme"),
    ("home", "NavbarSettings", "navbar_theme"),
    ("home", "FooterSettings", "footer_theme"),
]


def replace_themes(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")

    old_themes = list(ColorTheme.objects.all())
    if not old_themes:
        ColorTheme.objects.create(**LIGHT_THEME_DATA)
        return

    old_pks = [t.pk for t in old_themes]

    # Create the Light theme
    light = ColorTheme.objects.create(**LIGHT_THEME_DATA)

    # Re-point all FK references from old themes to the Light theme
    for app_label, model_name, field_name in THEME_FK_FIELDS:
        Model = apps.get_model(app_label, model_name)
        Model._default_manager.filter(
            **{f"{field_name}__in": old_pks}
        ).update(**{field_name: light})

    # Delete old themes
    ColorTheme.objects.filter(pk__in=old_pks).delete()


def reverse_replace(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    light = ColorTheme.objects.filter(name="Light").first()
    if light:
        light.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0049_blogindexpage_blogindexitem"),
    ]

    operations = [
        migrations.RunPython(replace_themes, reverse_replace),
    ]
