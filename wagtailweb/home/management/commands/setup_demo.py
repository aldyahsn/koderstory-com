from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from wagtail.models import Site

from home.models import (
    DesignSystemSettings,
    HomeClientLogo,
    HomeFeature,
    HomePage,
)


class Command(BaseCommand):
    help = "Set up demo homepage content and a local admin account."

    def handle(self, *args, **options):
        homepage = HomePage.objects.first()
        if homepage is None:
            self.stdout.write(self.style.ERROR("No HomePage exists. Run migrate first."))
            return

        homepage.hero_announcement = "Announcing our next product update."
        homepage.hero_announcement_link_label = "Read more"
        homepage.hero_announcement_link_url = "#features"
        homepage.hero_title = "Build a better digital experience"
        homepage.hero_description = (
            "Create clear, maintainable websites with fixed sections, flexible "
            "layouts, and an editor your team can understand."
        )
        homepage.hero_primary_button_label = "Get started"
        homepage.hero_primary_button_url = "#cta"
        homepage.hero_secondary_button_label = "Learn more"
        homepage.hero_secondary_button_url = "#features"

        homepage.clients_title = "Trusted by innovative teams"
        homepage.clients_description = (
            "A reusable client section with several layout options."
        )
        homepage.clients_cta_text = "Join teams building clearer digital products."
        homepage.clients_cta_label = "Read customer stories"
        homepage.clients_cta_url = "#features"
        homepage.clients_primary_button_label = "Create account"
        homepage.clients_primary_button_url = "#cta"
        homepage.clients_secondary_button_label = "Contact us"
        homepage.clients_secondary_button_url = "#cta"

        homepage.features_eyebrow = "Deploy faster"
        homepage.features_title = "Everything you need to build with confidence"
        homepage.features_description = (
            "Choose a feature layout that matches the components your story needs."
        )
        homepage.features_button_label = "Get started"
        homepage.features_button_url = "#cta"
        homepage.features_testimonial_quote = (
            "The fixed-section editor gives our team flexibility without losing structure."
        )
        homepage.features_testimonial_name = "Maria Hill"
        homepage.features_testimonial_role = "Product Manager"

        homepage.cta_eyebrow = "Start today"
        homepage.cta_title = "Ready to build your next Wagtail website?"
        homepage.cta_description = (
            "Use global design settings and section layouts to move quickly."
        )
        homepage.cta_primary_button_label = "Get started"
        homepage.cta_primary_button_url = "/admin/"
        homepage.cta_secondary_button_label = "View features"
        homepage.cta_secondary_button_url = "#features"
        homepage.save()

        if not homepage.client_logos.exists():
            for name in ["Transistor", "Reform", "Tuple", "SavvyCal", "Statamic", "Laravel"]:
                HomeClientLogo.objects.create(page=homepage, name=name)

        if not homepage.features.exists():
            feature_data = [
                ("PD", "Push to deploy", "Publish confidently with a clear workflow."),
                ("SC", "SSL certificates", "Keep every environment protected."),
                ("SQ", "Simple queues", "Run background work without extra complexity."),
                ("AS", "Advanced security", "Apply practical controls across the platform."),
                ("API", "Powerful API", "Connect the tools your business already uses."),
                ("DB", "Database backups", "Protect important data with reliable backups."),
            ]
            for icon, title, description in feature_data:
                HomeFeature.objects.create(
                    page=homepage,
                    icon=icon,
                    title=title,
                    description=description,
                    link_label="Learn more",
                    link_url="#cta",
                )

        site = Site.objects.filter(is_default_site=True).first() or Site.objects.first()
        if site:
            DesignSystemSettings.objects.get_or_create(site=site)

        user_model = get_user_model()
        admin, created = user_model.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password("admin")
        admin.save()

        status = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Demo content ready; admin user {status}."))
