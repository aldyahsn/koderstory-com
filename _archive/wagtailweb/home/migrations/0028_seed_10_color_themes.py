from django.db import migrations

THEMES = [
    {
        "name": "Default",
        # all blank — inherits hardcoded defaults
    },
    {
        "name": "Dark",
        "brand_color": "#818cf8",
        "primary_color": "#818cf8",
        "secondary_color": "#64748b",
        "accent_color": "#f472b6",
        "background_color": "#0f172a",
        "surface_color": "#1e293b",
        "surface_variant_color": "#334155",
        "text_color": "#f1f5f9",
        "text_muted_color": "#94a3b8",
        "text_on_brand_color": "#0f172a",
        "overlay_color": "#0f172a",
        "overlay_opacity": 80,
    },
    {
        "name": "Forest",
        "brand_color": "#059669",
        "primary_color": "#059669",
        "secondary_color": "#65a30d",
        "accent_color": "#fbbf24",
        "background_color": "#f0fdf4",
        "surface_color": "#dcfce7",
        "surface_variant_color": "#bbf7d0",
        "text_color": "#052e16",
        "text_muted_color": "#4a7c59",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#022c22",
        "overlay_opacity": 70,
    },
    {
        "name": "Ocean",
        "brand_color": "#0891b2",
        "primary_color": "#0891b2",
        "secondary_color": "#06b6d4",
        "accent_color": "#2dd4bf",
        "background_color": "#ecfeff",
        "surface_color": "#cffafe",
        "surface_variant_color": "#a5f3fc",
        "text_color": "#083344",
        "text_muted_color": "#3b82a0",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#083344",
        "overlay_opacity": 70,
    },
    {
        "name": "Sunset",
        "brand_color": "#ea580c",
        "primary_color": "#ea580c",
        "secondary_color": "#f97316",
        "accent_color": "#facc15",
        "background_color": "#fff7ed",
        "surface_color": "#ffedd5",
        "surface_variant_color": "#fed7aa",
        "text_color": "#431407",
        "text_muted_color": "#9a5b3a",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#431407",
        "overlay_opacity": 70,
    },
    {
        "name": "Lavender",
        "brand_color": "#7c3aed",
        "primary_color": "#7c3aed",
        "secondary_color": "#a78bfa",
        "accent_color": "#f472b6",
        "background_color": "#faf5ff",
        "surface_color": "#f3e8ff",
        "surface_variant_color": "#e9d5ff",
        "text_color": "#2e1065",
        "text_muted_color": "#7c4fa0",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#2e1065",
        "overlay_opacity": 70,
    },
    {
        "name": "Crimson",
        "brand_color": "#dc2626",
        "primary_color": "#dc2626",
        "secondary_color": "#ef4444",
        "accent_color": "#facc15",
        "background_color": "#fef2f2",
        "surface_color": "#fee2e2",
        "surface_variant_color": "#fecaca",
        "text_color": "#450a0a",
        "text_muted_color": "#a04040",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#450a0a",
        "overlay_opacity": 70,
    },
    {
        "name": "Slate",
        "brand_color": "#475569",
        "primary_color": "#475569",
        "secondary_color": "#64748b",
        "accent_color": "#94a3b8",
        "background_color": "#f8fafc",
        "surface_color": "#f1f5f9",
        "surface_variant_color": "#e2e8f0",
        "text_color": "#0f172a",
        "text_muted_color": "#64748b",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#0f172a",
        "overlay_opacity": 70,
    },
    {
        "name": "Amber",
        "brand_color": "#d97706",
        "primary_color": "#d97706",
        "secondary_color": "#f59e0b",
        "accent_color": "#fbbf24",
        "background_color": "#fffbeb",
        "surface_color": "#fef3c7",
        "surface_variant_color": "#fde68a",
        "text_color": "#451a03",
        "text_muted_color": "#926d28",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#451a03",
        "overlay_opacity": 70,
    },
    {
        "name": "Mint",
        "brand_color": "#0d9488",
        "primary_color": "#0d9488",
        "secondary_color": "#14b8a6",
        "accent_color": "#a3e635",
        "background_color": "#f0fdfa",
        "surface_color": "#ccfbf1",
        "surface_variant_color": "#99f6e4",
        "text_color": "#022c22",
        "text_muted_color": "#3b7970",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#022c22",
        "overlay_opacity": 70,
    },
    {
        "name": "Rose",
        "brand_color": "#e11d48",
        "primary_color": "#e11d48",
        "secondary_color": "#f43f5e",
        "accent_color": "#fbbf24",
        "background_color": "#fff1f2",
        "surface_color": "#ffe4e6",
        "surface_variant_color": "#fecdd3",
        "text_color": "#4c0519",
        "text_muted_color": "#a8455a",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#4c0519",
        "overlay_opacity": 70,
    },
    {
        "name": "Copper",
        "brand_color": "#b45309",
        "primary_color": "#b45309",
        "secondary_color": "#d97706",
        "accent_color": "#f59e0b",
        "background_color": "#fefce8",
        "surface_color": "#fef9c3",
        "surface_variant_color": "#fef08a",
        "text_color": "#292524",
        "text_muted_color": "#78716c",
        "text_on_brand_color": "#ffffff",
        "overlay_color": "#292524",
        "overlay_opacity": 70,
    },
]

ALL_THEME_NAMES = [t["name"] for t in THEMES]


def seed_themes(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    existing = set(ColorTheme.objects.values_list("name", flat=True))
    for data in THEMES:
        if data["name"] in existing:
            continue
        ColorTheme.objects.create(**data)


def reverse_seed(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    ColorTheme.objects.filter(name__in=ALL_THEME_NAMES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0027_alter_homepage_clients_theme_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_themes, reverse_seed),
    ]
