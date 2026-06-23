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
    button_url = blocks.URLBlock(required=False, default="", help_text="Form action URL.")

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
    fallback_image_url = blocks.URLBlock(required=False, default="", help_text="Used when no Wagtail image is selected.")
    image_alt = blocks.CharBlock(required=False, max_length=140)
    link_label = blocks.CharBlock(required=False, max_length=80)
    link_url = blocks.CharBlock(required=False, max_length=255, default="")
    meta = blocks.CharBlock(required=False, max_length=120)

    class Meta:
        icon = "form"
        label = "Card"


class DarkFlatTextSectionBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, max_length=80)
    heading = blocks.CharBlock(required=False, max_length=180)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    fallback_image_url = blocks.URLBlock(required=False, default="")
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
    fallback_image_url = blocks.URLBlock(required=False, default="", help_text="Used when no Wagtail image is selected.")
    image_alt = blocks.CharBlock(required=False, max_length=140)
    url = blocks.CharBlock(required=False, max_length=255, default="")

    class Meta:
        icon = "image"
        label = "Client logo"


class DarkFlatClientListBlock(blocks.StreamBlock):
    client = DarkFlatClientBlock()

    class Meta:
        label = "Client list"


class SectionButtonBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=80)
    url = blocks.CharBlock(required=False, max_length=255, default="")

    class Meta:
        icon = "link"
        label = "Button"


class SectionMediaBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    fallback_image_url = blocks.URLBlock(required=False, default="")
    image_alt = blocks.CharBlock(required=False, max_length=140)

    class Meta:
        icon = "image"
        label = "Media"


class SectionCardBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, max_length=80)
    title = blocks.CharBlock(max_length=180)
    description = blocks.RichTextBlock(required=False)
    icon = blocks.CharBlock(required=False, max_length=16)
    media = SectionMediaBlock(required=False)
    link_label = blocks.CharBlock(required=False, max_length=80)
    link_url = blocks.CharBlock(required=False, max_length=255, default="")
    meta = blocks.CharBlock(required=False, max_length=140)

    class Meta:
        icon = "form"
        label = "Card"


class SectionTextItemBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, max_length=80)
    heading = blocks.CharBlock(required=False, max_length=180)
    body = blocks.RichTextBlock(required=False)
    media = SectionMediaBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Text item"


class SectionLogoBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, max_length=100)
    media = SectionMediaBlock(required=False)
    url = blocks.CharBlock(required=False, max_length=255, default="")

    class Meta:
        icon = "image"
        label = "Logo"


class SectionHeroBlock(blocks.StructBlock):
    STYLE_CHOICES = [
        ("cover", "Cover background"),
        ("split", "Split media"),
        ("simple", "Simple"),
    ]
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="hero")
    style = blocks.ChoiceBlock(choices=STYLE_CHOICES, default="cover")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(max_length=220)
    description = blocks.RichTextBlock(required=False)
    side_note = blocks.RichTextBlock(required=False)
    primary_button = SectionButtonBlock(required=False)
    secondary_button = SectionButtonBlock(required=False)
    media = SectionMediaBlock(required=False)
    gallery = blocks.ListBlock(SectionMediaBlock(), required=False)

    class Meta:
        icon = "title"
        label = "Hero"


class SectionClientsBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="clients")
    heading = blocks.CharBlock(required=False, max_length=180)
    logos = blocks.ListBlock(SectionLogoBlock(), required=False)

    class Meta:
        icon = "group"
        label = "Client logo row"


class SectionContentBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="content")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(required=False, max_length=220)
    description = blocks.RichTextBlock(required=False)
    items = blocks.ListBlock(SectionTextItemBlock(), required=False)

    class Meta:
        icon = "doc-full"
        label = "Content"


class SectionCardsBlock(blocks.StructBlock):
    STYLE_CHOICES = [
        ("grid", "Grid cards"),
        ("horizontal", "Horizontal service list"),
        ("checklist", "Checklist panel"),
        ("featured", "Featured card then grid"),
        ("work", "Work mosaic"),
        ("steps", "Step cards"),
    ]
    COLUMN_CHOICES = [
        ("two", "Two columns"),
        ("three", "Three columns"),
    ]
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="list")
    style = blocks.ChoiceBlock(choices=STYLE_CHOICES, default="grid")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(required=False, max_length=220)
    description = blocks.RichTextBlock(required=False)
    columns = blocks.ChoiceBlock(choices=COLUMN_CHOICES, default="three")
    cards = blocks.ListBlock(SectionCardBlock(), required=False)

    class Meta:
        icon = "grip"
        label = "Cards"


class SectionArticleBodyStreamBlock(blocks.StreamBlock):
    section = SectionTextItemBlock()
    quote = blocks.RichTextBlock(required=False)

    class Meta:
        label = "Article body"


class SectionArticleBodyBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="article")
    meta = blocks.CharBlock(required=False, max_length=160)
    cover = SectionMediaBlock(required=False)
    body = SectionArticleBodyStreamBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Article body"


class SectionWorkSummaryBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="summary")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(required=False, max_length=220)
    description = blocks.RichTextBlock(required=False)
    facts = blocks.ListBlock(SectionCardBlock(), required=False)
    media = SectionMediaBlock(required=False)

    class Meta:
        icon = "clipboard-list"
        label = "Work summary"


class SectionContactBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="contact")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(required=False, max_length=220)
    description = blocks.RichTextBlock(required=False)
    cards = blocks.ListBlock(SectionCardBlock(), required=False)

    class Meta:
        icon = "mail"
        label = "Contact intro"


class SectionCtaBlock(blocks.StructBlock):
    anchor_id = blocks.CharBlock(required=False, max_length=40, default="next-step")
    eyebrow = blocks.CharBlock(required=False, max_length=120)
    title = blocks.CharBlock(max_length=220)
    description = blocks.RichTextBlock(required=False)
    primary_button = SectionButtonBlock(required=False)
    secondary_button = SectionButtonBlock(required=False)

    class Meta:
        icon = "pick"
        label = "CTA"


class SectionPageSectionsBlock(blocks.StreamBlock):
    hero = SectionHeroBlock()
    clients = SectionClientsBlock()
    content = SectionContentBlock()
    cards = SectionCardsBlock()
    article_body = SectionArticleBodyBlock()
    work_summary = SectionWorkSummaryBlock()
    contact = SectionContactBlock()
    cta = SectionCtaBlock()

    class Meta:
        label = "Page sections"
