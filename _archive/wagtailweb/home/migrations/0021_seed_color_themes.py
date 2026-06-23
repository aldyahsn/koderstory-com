from django.db import migrations


def seed_themes(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    if not ColorTheme.objects.filter(name="Default").exists():
        ColorTheme.objects.create(name="Default")
    if not ColorTheme.objects.filter(name="Dark").exists():
        ColorTheme.objects.create(
            name="Dark",
            brand_color="#818cf8",
            primary_color="#818cf8",
            secondary_color="#64748b",
            accent_color="#f472b6",
            background_color="#0f172a",
            surface_color="#1e293b",
            surface_variant_color="#334155",
            text_color="#f1f5f9",
            text_muted_color="#94a3b8",
            text_on_brand_color="#0f172a",
            overlay_color="#0f172a",
            overlay_opacity=80,
        )


def reverse_seed(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    ColorTheme.objects.filter(name__in=["Default", "Dark"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_colortheme_homepage_clients_theme_homepage_cta_theme_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_themes, reverse_seed),
    ]
