from django.db import migrations

OLD_TO_NEW = {
    "narrow": "compact",
    "compact": "compact",
    "normal": "normal",
    "wide": "spacious",
    "large": "spacious",
    "spacious": "spacious",
    "full": "full",
}


def migrate_forward(apps, schema_editor):
    HomePage = apps.get_model("home", "HomePage")
    for page in HomePage.objects.all():
        for prefix in ("hero", "clients", "features", "cta"):
            field = f"{prefix}_section_height"
            old = getattr(page, field, "")
            new = OLD_TO_NEW.get(old, "normal")
            if old != new:
                setattr(page, field, new)
        page.save(update_fields=[
            f"{p}_section_height" for p in ("hero", "clients", "features", "cta")
        ])


def migrate_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_homepage_clients_section_height_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_reverse),
    ]
