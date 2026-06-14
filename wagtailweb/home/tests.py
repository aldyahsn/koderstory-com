import json

from wagtail.admin.rich_text.converters.contentstate import ContentstateConverter
from wagtail.models import Page, Site
from wagtail.test.utils import WagtailPageTestCase

from home.models import (
    RICH_TEXT_FEATURES,
    DesignSystemSettings,
    HomeFeature,
    HomePage,
)


class HomeTests(WagtailPageTestCase):
    def setUp(self):
        root = Page.get_first_root_node()
        self.site = Site.objects.create(
            hostname="testsite",
            root_page=root,
            is_default_site=True,
        )
        self.homepage = HomePage(
            title="Home",
            hero_title="Build a better website",
            hero_description="A fixed-section Wagtail homepage.",
            clients_title="Trusted by teams",
            features_title="Everything you need",
            cta_title="Start your project",
        )
        root.add_child(instance=self.homepage)
        HomeFeature.objects.create(
            page=self.homepage,
            title="Fast setup",
            description="Start with a reliable structure.",
        )

    def test_homepage_is_renderable(self):
        self.assertPageIsRenderable(self.homepage)

    def test_homepage_template_used(self):
        response = self.client.get(self.homepage.url)
        self.assertTemplateUsed(response, "home/home_page.html")

    def test_each_variant_family_has_expected_count(self):
        self.assertEqual(len(HomePage.HERO_VARIANTS), 6)
        self.assertEqual(len(HomePage.CLIENTS_VARIANTS), 5)
        self.assertEqual(len(HomePage.FEATURES_VARIANTS), 12)
        self.assertEqual(len(HomePage.CTA_VARIANTS), 4)

    def test_variant_metadata_declares_components_and_template(self):
        variant_sets = [
            HomePage.HERO_VARIANTS,
            HomePage.CLIENTS_VARIANTS,
            HomePage.FEATURES_VARIANTS,
            HomePage.CTA_VARIANTS,
        ]
        for variants in variant_sets:
            for variant in variants.values():
                self.assertTrue(variant["components"])
                self.assertTrue(variant["template"].endswith(".html"))

    def test_layout_switches_template(self):
        self.homepage.hero_layout = HomePage.HERO_ANGLED_MEDIA_RIGHT
        self.homepage.save(update_fields=["hero_layout"])
        response = self.client.get(self.homepage.url)
        self.assertTemplateUsed(
            response,
            "home/sections/hero/angled_media_right.html",
        )

    def test_section_can_be_disabled(self):
        self.homepage.features_enabled = False
        self.homepage.save(update_fields=["features_enabled"])
        response = self.client.get(self.homepage.url)
        self.assertNotContains(response, 'id="features"')

    def test_editor_has_content_and_section_settings_tabs(self):
        edit_handler = HomePage.get_edit_handler()
        self.assertEqual(
            [panel.heading for panel in edit_handler.children],
            ["Content", "Section settings", "Promote", "Settings"],
        )
        form_class = edit_handler.get_form_class()
        for field_name in [
            "hero_layout",
            "clients_layout",
            "features_layout",
            "cta_layout",
        ]:
            self.assertIn(field_name, form_class.base_fields)

    def test_global_design_settings_model_is_available(self):
        settings = DesignSystemSettings(
            site=self.site,
            brand_color="#123456",
        )
        settings.save()
        self.assertEqual(settings.brand_color, "#123456")

    def test_global_settings_editor_is_organized_into_tabs(self):
        self.assertEqual(DesignSystemSettings._meta.verbose_name, "Global settings")
        self.assertEqual(
            [panel.heading for panel in DesignSystemSettings.edit_handler.children],
            ["Typography", "Colors", "Layout & components"],
        )

    def test_rich_text_alignment_features_round_trip_bootstrap_classes(self):
        alignment_features = ["align-left", "align-center", "align-right"]
        for feature in alignment_features:
            self.assertIn(feature, RICH_TEXT_FEATURES)

        converter = ContentstateConverter(features=alignment_features)
        contentstate = json.loads(
            converter.from_database_format(
                '<p class="text-start">Left</p>'
                '<p class="text-center">Center</p>'
                '<p class="text-end">Right</p>'
            )
        )
        self.assertEqual(
            [block["type"] for block in contentstate["blocks"]],
            alignment_features,
        )

        rendered = converter.to_database_format(json.dumps(contentstate))
        self.assertIn('class="text-start"', rendered)
        self.assertIn('class="text-center"', rendered)
        self.assertIn('class="text-end"', rendered)
