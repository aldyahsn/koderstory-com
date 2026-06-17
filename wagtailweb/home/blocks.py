from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

WIDTH_CHOICES = [
    (25, "25%"),
    (33, "33%"),
    (50, "50%"),
    (66, "66%"),
    (75, "75%"),
    (100, "100%"),
]


class NavigationColumnBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=WIDTH_CHOICES, default=25)
    heading = blocks.CharBlock(required=False, max_length=80)
    nav_group = SnippetChooserBlock("home.NavigationLinkGroup")

    class Meta:
        icon = "list-ul"
        label = "Navigation"


class SocialColumnBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=WIDTH_CHOICES, default=25)
    heading = blocks.CharBlock(required=False, max_length=80)
    social_group = SnippetChooserBlock("home.SocialMediaGroup")
    icon_size = blocks.ChoiceBlock(
        choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
        default="medium",
    )
    icon_position = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="left",
    )

    class Meta:
        icon = "group"
        label = "Social"


class NewsletterColumnBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=WIDTH_CHOICES, default=25)
    heading = blocks.CharBlock(required=False, max_length=80)
    description = blocks.RichTextBlock(required=False)
    placeholder_text = blocks.CharBlock(required=False, default="Your email")
    button_label = blocks.CharBlock(required=False, default="Subscribe")
    button_url = blocks.URLBlock(required=False, help_text="Form action URL.")

    class Meta:
        icon = "mail"
        label = "Newsletter"


class TextColumnBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=WIDTH_CHOICES, default=25)
    heading = blocks.CharBlock(required=False, max_length=80)
    body = blocks.RichTextBlock()

    class Meta:
        icon = "doc-full"
        label = "Text"


class ImageColumnBlock(blocks.StructBlock):
    width = blocks.ChoiceBlock(choices=WIDTH_CHOICES, default=25)
    heading = blocks.CharBlock(required=False, max_length=80)
    image = ImageChooserBlock()
    image_height = blocks.IntegerBlock(
        required=False, label="Max height (px)",
        help_text="Leave blank for natural height.",
    )
    image_position = blocks.ChoiceBlock(
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="left",
        label="Alignment",
    )

    class Meta:
        icon = "image"
        label = "Image"


class FooterColumnsBlock(blocks.StreamBlock):
    navigation = NavigationColumnBlock()
    social = SocialColumnBlock()
    newsletter = NewsletterColumnBlock()
    text = TextColumnBlock()
    image = ImageColumnBlock()

    class Meta:
        label = "Footer columns"


class DarkFlatCardBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, max_length=80)
    title = blocks.CharBlock(max_length=160)
    description = blocks.RichTextBlock(required=False)
    icon = blocks.CharBlock(required=False, max_length=16, help_text="Emoji, number, or short label.")
    image = ImageChooserBlock(required=False)
    fallback_image_url = blocks.URLBlock(required=False, help_text="Used when no Wagtail image is selected.")
    image_alt = blocks.CharBlock(required=False, max_length=140)
    link_label = blocks.CharBlock(required=False, max_length=80)
    link_url = blocks.CharBlock(required=False, max_length=255)
    meta = blocks.CharBlock(required=False, max_length=120)

    class Meta:
        icon = "form"
        label = "Card"


class DarkFlatTextSectionBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, max_length=80)
    heading = blocks.CharBlock(required=False, max_length=180)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    fallback_image_url = blocks.URLBlock(required=False)
    image_alt = blocks.CharBlock(required=False, max_length=140)

    class Meta:
        icon = "doc-full"
        label = "Text section"


class DarkFlatBodyBlock(blocks.StreamBlock):
    section = DarkFlatTextSectionBlock()
    card = DarkFlatCardBlock()

    class Meta:
        label = "Body content"


class DarkFlatCardListBlock(blocks.StreamBlock):
    card = DarkFlatCardBlock()

    class Meta:
        label = "Cards"


class DarkFlatClientBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    fallback_image_url = blocks.URLBlock(required=False, help_text="Used when no Wagtail image is selected.")
    image_alt = blocks.CharBlock(required=False, max_length=140)
    url = blocks.CharBlock(required=False, max_length=255)

    class Meta:
        icon = "image"
        label = "Client logo"


class DarkFlatClientListBlock(blocks.StreamBlock):
    client = DarkFlatClientBlock()

    class Meta:
        label = "Client list"
