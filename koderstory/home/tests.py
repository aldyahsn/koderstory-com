from wagtail.models import Page, Site
from wagtail.test.utils import WagtailPageTestCase

from home.models import HomeClientLogo, HomePage, HomeProductCard, HomeServiceCard


HOMEPAGE_DEFAULTS = {
    "hero_anchor_id": "hero",
    "hero_eyebrow": "Custom digital systems",
    "hero_title": "Practical digital systems for business operations and growth",
    "hero_description": (
        "Koderstory builds custom web applications, ERP workflows, dashboards, "
        "mobile tools, and automation systems that help businesses organize "
        "operations and grow with clearer systems."
    ),
    "hero_primary_button_label": "Start project",
    "hero_primary_button_url": "#contact",
    "hero_secondary_button_label": "View work",
    "hero_secondary_button_url": "#services",
    "clients_anchor_id": "clients",
    "clients_title": "Experience across digital products and operations",
    "services_anchor_id": "services",
    "services_kicker": "Services",
    "services_title": "Build the right system for the right business need",
    "services_description": "Start from your current workflow, problem, or operational bottleneck.",
    "services_button_label": "View all services",
    "services_button_url": "#contact",
    "products_anchor_id": "products",
    "products_kicker": "Products",
    "products_title": "Products and solution concepts",
    "products_button_label": "View all products",
    "products_button_url": "#contact",
    "cta_anchor_id": "cta",
    "cta_kicker": "Start a project",
    "cta_title": "Need a practical system for your business?",
    "cta_description": "Start with your process, problem, or product idea.",
    "cta_primary_button_label": "Fill project form",
    "cta_primary_button_url": "#contact",
    "cta_secondary_button_label": "Contact",
    "cta_secondary_button_url": "mailto:aldy@koderstory.com",
}


def add_homepage_children(homepage):
    for name in ["Client 01", "Client 02", "Client 03", "Client 04"]:
        HomeClientLogo.objects.create(page=homepage, name=name)

    service_cards = [
        (
            "Web app",
            "Custom Web Application",
            "Business systems, portals, internal tools, and operational workflows.",
        ),
        (
            "ERP",
            "Odoo / ERP",
            "ERP implementation, workflow customization, and operations improvement.",
        ),
        (
            "Dashboard",
            "Business Dashboard",
            "Reporting and KPI visibility for operations, finance, and decision making.",
        ),
    ]
    for eyebrow, title, description in service_cards:
        HomeServiceCard.objects.create(
            page=homepage,
            eyebrow=eyebrow,
            title=title,
            description=description,
            button_label="View service",
            button_url="#contact",
        )

    product_cards = [
        (
            "Hospitality",
            "SIRASA",
            "Hotel and partner merchant QR ordering system concept.",
        ),
        (
            "Education",
            "BIMORA",
            "Management system concept for tutoring and education administration.",
        ),
    ]
    for eyebrow, title, description in product_cards:
        HomeProductCard.objects.create(
            page=homepage,
            eyebrow=eyebrow,
            title=title,
            description=description,
            button_label="View product",
            button_url="#contact",
        )


class HomeSetUpTests(WagtailPageTestCase):
    def test_root_create(self):
        root_page = Page.objects.get(pk=1)
        self.assertIsNotNone(root_page)

    def test_homepage_create(self):
        root_page = Page.objects.get(pk=1)
        homepage = HomePage(title="Home", **HOMEPAGE_DEFAULTS)
        root_page.add_child(instance=homepage)
        add_homepage_children(homepage)
        self.assertTrue(HomePage.objects.filter(title="Home").exists())
        self.assertEqual(homepage.service_cards.count(), 3)


class HomeTests(WagtailPageTestCase):
    def setUp(self):
        root_page = Page.get_first_root_node()
        Site.objects.create(hostname="testsite", root_page=root_page, is_default_site=True)
        self.homepage = HomePage(title="Home", **HOMEPAGE_DEFAULTS)
        root_page.add_child(instance=self.homepage)
        add_homepage_children(self.homepage)

    def test_homepage_is_renderable(self):
        self.assertPageIsRenderable(self.homepage)

    def test_homepage_template_used(self):
        response = self.client.get(self.homepage.url)
        self.assertTemplateUsed(response, "home/home_page.html")

    def test_homepage_renders_landing_sections(self):
        response = self.client.get(self.homepage.url)
        self.assertContains(
            response,
            "Practical digital systems for business operations and growth",
        )
        self.assertContains(response, "Custom Web Application")
        self.assertContains(response, "SIRASA")
        self.assertContains(response, "Need a practical system for your business?")
