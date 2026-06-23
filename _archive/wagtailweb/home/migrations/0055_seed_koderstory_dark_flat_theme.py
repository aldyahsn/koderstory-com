from django.db import migrations


DARK_FLAT_THEME = {
    "name": "Koderstory Dark Flat",
    "is_default": True,
    "body_text_color": "#ffffff",
    "heading_text_color": "#ffffff",
    "muted_text_color": "#ffffffad",
    "link_color": "#00c49a",
    "link_hover_color": "#ffffff",
    "button_primary_bg": "#00c49a",
    "button_primary_hover": "#ffffff",
    "button_secondary_border": "#ffffff38",
    "button_secondary_hover_bg": "#ffffff",
    "page_bg": "#05070d",
    "surface_bg": "#0b0f19",
    "surface_border": "#ffffff24",
    "feature_icon_bg": "#00c49a",
    "feature_icon_text": "#03110e",
    "check_color": "#00c49a",
    "brand_glow": "#00c49a",
    "navbar_bg": "#05070d",
    "navbar_text_color": "#ffffff",
    "navbar_link_color": "#ffffffad",
    "navbar_link_hover_color": "#ffffff",
    "footer_bg": "#05070d",
    "footer_text_color": "#ffffffad",
    "footer_heading_color": "#ffffff",
    "footer_link_color": "#ffffff",
    "footer_link_hover_color": "#00c49a",
}


def seed_dark_flat_theme(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    DesignSystemSettings = apps.get_model("home", "DesignSystemSettings")
    NavbarSettings = apps.get_model("home", "NavbarSettings")
    FooterSettings = apps.get_model("home", "FooterSettings")
    NavigationLinkGroup = apps.get_model("home", "NavigationLinkGroup")
    NavigationLink = apps.get_model("home", "NavigationLink")

    ColorTheme.objects.exclude(name=DARK_FLAT_THEME["name"]).update(is_default=False)
    theme, _ = ColorTheme.objects.update_or_create(
        name=DARK_FLAT_THEME["name"],
        defaults=DARK_FLAT_THEME,
    )

    nav_group, _ = NavigationLinkGroup.objects.get_or_create(
        name="Koderstory Main Navigation"
    )
    if not nav_group.links.exists():
        for sort_order, (label, url) in enumerate(
            [
                ("Home", "/"),
                ("Services", "/services/"),
                ("Industries", "/industries/"),
                ("Work", "/work/"),
                ("Resources", "/resources/"),
                ("About", "/about/"),
            ]
        ):
            NavigationLink.objects.create(
                group=nav_group,
                label=label,
                url=url,
                sort_order=sort_order,
            )

    for settings in DesignSystemSettings.objects.all():
        settings.global_theme = theme
        settings.heading_font = "Poppins"
        settings.body_font = "Nunito Sans"
        settings.base_font_size = 18
        settings.line_height = 1.8
        settings.letter_spacing = "-0.5px"
        settings.section_padding = 104
        settings.container_width = 1320
        settings.button_radius = 999
        settings.card_radius = 24
        settings.input_radius = 8
        settings.button_border_width = 1
        settings.save()

    for settings in NavbarSettings.objects.all():
        settings.logo_text = "Koderstory"
        settings.sticky = True
        settings.nav_transparent = True
        settings.nav_scroll_animation = "none"
        settings.cta_label = "Konsultasikan Sistem"
        settings.cta_url = "/contact/"
        settings.nav_group = nav_group
        settings.navbar_theme = theme
        settings.save()

    for settings in FooterSettings.objects.all():
        settings.footer_theme = theme
        settings.section_height = "normal"
        settings.content_width = "normal"
        settings.copyright_text = "PT. koderstory software indonesia. All rights reserved."
        settings.save()


def reverse_seed_dark_flat_theme(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    ColorTheme.objects.filter(name=DARK_FLAT_THEME["name"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0054_alter_designsystemsettings_body_font_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_dark_flat_theme, reverse_seed_dark_flat_theme),
    ]
