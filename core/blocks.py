from django.core.exceptions import ValidationError
from wagtail import blocks
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.images.blocks import ImageChooserBlock


HERO_VARIANTS = (
    ("centered", "Centered"),
    ("image_right", "Image right"),
    ("dark", "Dark"),
)


class HeroBlock(blocks.StructBlock):
    variant = blocks.ChoiceBlock(choices=HERO_VARIANTS, default="centered")
    eyebrow = blocks.CharBlock(max_length=120, required=False)
    heading = blocks.CharBlock(max_length=180)
    body = blocks.RichTextBlock(
        features=["bold", "italic", "link"],
        required=False,
    )
    primary_button_text = blocks.CharBlock(max_length=80, required=False)
    primary_button_url = blocks.URLBlock(required=False)
    secondary_button_text = blocks.CharBlock(max_length=80, required=False)
    secondary_button_url = blocks.URLBlock(required=False)
    image = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(max_length=160, required=False)

    def clean(self, value):
        cleaned = super().clean(value)
        if cleaned.get("variant") == "image_right" and not cleaned.get("image"):
            if self.is_deferred_validation:
                return cleaned
            raise StructBlockValidationError(
                block_errors={
                    "image": ValidationError(
                        "The image right hero needs an image before publishing."
                    )
                }
            )
        return cleaned

    class Meta:
        icon = "home"
        label = "Hero"
        template = "blocks/hero.html"
        preview_template = "blocks/preview.html"
        preview_value = {
            "variant": "image_right",
            "eyebrow": "Bootstrap 5.3",
            "heading": "Build a Bootstrap-style hero in Wagtail",
            "body": "Start with one hero block, then extend the builder one piece at a time.",
            "primary_button_text": "Get started",
            "primary_button_url": "https://getbootstrap.com/docs/5.3/examples/heroes/",
            "secondary_button_text": "Learn more",
            "secondary_button_url": "https://getbootstrap.com/docs/5.3/getting-started/introduction/",
        }
        description = "Bootstrap-inspired hero section with centered, image, and dark variants."


class PageBodyStreamBlock(blocks.StreamBlock):
    hero = HeroBlock()

    class Meta:
        label = "Page sections"
