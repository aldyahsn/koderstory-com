from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from wagtail.models import Site

from home.models import (
    DesignSystemSettings,
    FooterSettings,
    HomeClientLogo,
    HomeFeature,
    HomePage,
    NavigationLink,
    NavigationLinkGroup,
    NavbarSettings,
    SocialLink,
    SocialMediaGroup,
)


class Command(BaseCommand):
    help = "Set up demo homepage content, navbar, footer, and a local admin account."

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
        if not site:
            self.stdout.write(self.style.ERROR("No site found."))
            return

        DesignSystemSettings.objects.get_or_create(site=site)

        # ── Clear existing navbar + footer seed data ──
        NavbarSettings.objects.filter(site=site).delete()
        FooterSettings.objects.filter(site=site).delete()
        NavigationLink.objects.all().delete()
        NavigationLinkGroup.objects.all().delete()
        SocialLink.objects.all().delete()
        SocialMediaGroup.objects.all().delete()

        # ── Seed navigation link group ──
        nav_group = NavigationLinkGroup.objects.create(name="Main navigation")
        nav_links = [
            ("Home", "/"),
            ("Features", "#features"),
            ("Pricing", "#cta"),
            ("About", "#"),
        ]
        for i, (label, url) in enumerate(nav_links, start=1):
            NavigationLink.objects.create(group=nav_group, label=label, url=url, sort_order=i)

        # ── Seed social media groups ──
        social_group = SocialMediaGroup.objects.create(name="Social media")
        social_links = [
            ("X", "https://x.com", "x", "filled"),
            ("GitHub", "https://github.com", "github", "filled"),
            ("LinkedIn", "https://linkedin.com", "linkedin", "filled"),
            ("YouTube", "https://youtube.com", "youtube", "outline"),
        ]
        for i, (label, url, platform, variant) in enumerate(social_links, start=1):
            SocialLink.objects.create(group=social_group, label=label, url=url, platform=platform, icon_variant=variant, sort_order=i)

        # ── Seed navbar settings ──
        NavbarSettings.objects.create(
            site=site,
            layout="logo_left_center",
            section_height=60,
            logo_text="KoderStory",
            sticky=True,
            nav_group=nav_group,
            cta_label="Get started",
            cta_url="#cta",
        )

        # ── Seed footer settings with StreamField columns ──
        FooterSettings.objects.create(
            site=site,
            section_height="compact",
            copyright_text="© 2026 KoderStory. All rights reserved.",
            bottom_bar=True,
            columns=[
                ("navigation", {
                    "width": 25,
                    "heading": "Links",
                    "nav_group": nav_group,
                }),
                ("social", {
                    "width": 25,
                    "heading": "Follow us",
                    "social_group": social_group,
                    "icon_size": "medium",
                    "icon_position": "left",
                }),
                ("newsletter", {
                    "width": 25,
                    "heading": "Stay updated",
                    "description": "<p>Get the latest news and updates.</p>",
                    "placeholder_text": "Your email",
                    "button_label": "Subscribe",
                    "button_url": "#",
                }),
                ("text", {
                    "width": 25,
                    "heading": "About",
                    "body": "<p>Building clear, maintainable websites with Wagtail.</p>",
                }),
            ],
        )

        # ── Admin user ──
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
        self.stdout.write(self.style.SUCCESS(f"Demo content + navbar + footer ready; admin user {status}."))
