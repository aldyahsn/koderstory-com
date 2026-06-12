from django.test import Client, TestCase
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.models import Site

from core.blocks import HeroBlock
from pages.models import HomePage


class HomePageSmokeTests(TestCase):
    def test_bootstrap_homepage_and_site_exist(self):
        self.assertTrue(HomePage.objects.exists())
        self.assertTrue(Site.objects.filter(hostname="localhost", port=8000).exists())

    def test_homepage_renders_through_wagtail_site(self):
        response = Client(HTTP_HOST="localhost:8000").get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bootstrap heroes for Wagtail")


class HeroBlockTests(TestCase):
    def test_image_right_variant_rejects_missing_image(self):
        block = HeroBlock()
        value = block.to_python(
            {
                "variant": "image_right",
                "eyebrow": "Bootstrap 5.3",
                "heading": "Responsive left-aligned hero with image",
                "body": "<p>Simple, focused hero content.</p>",
                "primary_button_text": "Primary",
                "primary_button_url": "https://example.com/primary",
                "secondary_button_text": "Secondary",
                "secondary_button_url": "https://example.com/secondary",
                "image": None,
                "image_alt": "",
            }
        )

        with self.assertRaises(StructBlockValidationError):
            block.clean(value)

    def test_centered_variant_allows_missing_image(self):
        block = HeroBlock()
        value = block.to_python(
            {
                "variant": "centered",
                "eyebrow": "Centered hero",
                "heading": "Build a Bootstrap-style hero in Wagtail",
                "body": "<p>Start with one block, then expand later.</p>",
                "primary_button_text": "Get started",
                "primary_button_url": "https://example.com/start",
                "secondary_button_text": "Learn more",
                "secondary_button_url": "https://example.com/learn",
                "image": None,
                "image_alt": "",
            }
        )

        cleaned = block.clean(value)
        self.assertEqual(cleaned["variant"], "centered")
