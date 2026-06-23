from django.db import migrations

BLANK_FIELDS = [
    "brand_color", "primary_color", "secondary_color", "accent_color",
    "success_color", "warning_color", "error_color", "info_color",
    "background_color", "surface_color", "surface_variant_color",
    "text_color", "text_muted_color", "text_on_brand_color",
    "overlay_color", "overlay_opacity",
]


def clear_default(apps, schema_editor):
    ColorTheme = apps.get_model("home", "ColorTheme")
    default = ColorTheme.objects.filter(name="Default").first()
    if default:
        for f in BLANK_FIELDS:
            setattr(default, f, None if f == "overlay_opacity" else "")
        default.save()


def reverse_clear(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0022_alter_colortheme_accent_color_and_more"),
    ]

    operations = [
        migrations.RunPython(clear_default, reverse_clear),
    ]
