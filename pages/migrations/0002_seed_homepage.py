from django.conf import settings
from django.db import migrations
from pages.models import HomePage
from wagtail.models import Locale, Page, Site


def create_homepage(apps, schema_editor):
    locale, _ = Locale.objects.get_or_create(language_code=settings.LANGUAGE_CODE)

    home_page = HomePage.objects.first()
    root_page = Page.objects.filter(depth=1).first()
    if root_page is None:
        root_page = Page.add_root(title="Root", slug="root", locale=locale)

    if home_page is None:
        home_page = HomePage(title="Koderstory Builder", slug="home", locale=locale)
        root_page.add_child(instance=home_page)

    home_page.body = [
        (
            "hero",
            {
                "variant": "centered",
                "eyebrow": "Bootstrap 5.3",
                "heading": "Bootstrap heroes for Wagtail",
                "body": "<p>Start with one hero block, then extend the builder one piece at a time.</p>",
                "primary_button_text": "Get started",
                "primary_button_url": "https://getbootstrap.com/docs/5.3/examples/heroes/",
                "secondary_button_text": "Learn more",
                "secondary_button_url": "https://getbootstrap.com/docs/5.3/getting-started/introduction/",
                "image": None,
                "image_alt": "",
            },
        )
    ]
    home_page.save_revision().publish()

    for hostname in ("localhost", "127.0.0.1"):
        Site.objects.update_or_create(
            hostname=hostname,
            port=8000,
            defaults={
                "site_name": "Koderstory Builder",
                "root_page": home_page,
            },
        )


def clear_homepage(apps, schema_editor):
    Site.objects.filter(hostname="localhost", port=8000).delete()
    HomePage.objects.filter(slug="home").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_homepage, clear_homepage),
    ]
