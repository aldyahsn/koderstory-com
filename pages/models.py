from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from core.blocks import PageBodyStreamBlock


class BodyStreamMixin(models.Model):
    body = StreamField(PageBodyStreamBlock(), blank=True)

    class Meta:
        abstract = True


class HomePage(BodyStreamMixin, Page):
    template = "pages/home_page.html"
    subpage_types = [
        "pages.FlexiblePage",
        "pages.BlogIndexPage",
        "pages.FormPage",
    ]

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class FlexiblePage(BodyStreamMixin, Page):
    template = "pages/flexible_page.html"
    parent_page_types = [
        "pages.HomePage",
        "pages.FlexiblePage",
    ]
    subpage_types = [
        "pages.FlexiblePage",
        "pages.FormPage",
    ]

    intro = RichTextField(blank=True, features=["bold", "italic", "link"])

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]


class BlogIndexPage(BodyStreamMixin, Page):
    template = "pages/blog_index_page.html"
    parent_page_types = ["pages.HomePage", "pages.FlexiblePage"]
    subpage_types = ["pages.BlogPostPage"]

    intro = RichTextField(blank=True, features=["bold", "italic", "link"])

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["posts"] = (
            BlogPostPage.objects.live()
            .public()
            .descendant_of(self)
            .order_by("-date", "-first_published_at")
        )
        return context


class BlogPostPage(BodyStreamMixin, Page):
    template = "pages/blog_post_page.html"
    parent_page_types = ["pages.BlogIndexPage"]
    subpage_types = []

    date = models.DateField("Post date")
    author = models.CharField(max_length=120, blank=True)
    summary = models.TextField(blank=True)
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("author"),
        FieldPanel("summary"),
        FieldPanel("cover_image"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("summary"),
        index.SearchField("body"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey(
        "FormPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class FormPage(BodyStreamMixin, AbstractEmailForm):
    template = "pages/form_page.html"
    parent_page_types = ["pages.HomePage", "pages.FlexiblePage"]
    subpage_types = []

    intro = RichTextField(blank=True, features=["bold", "italic", "link"])
    thank_you_text = RichTextField(blank=True, features=["bold", "italic", "link"])

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldPanel("to_address"),
                FieldPanel("from_address"),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    def get_landing_page_template(self, request, *args, **kwargs):
        return "pages/form_page_landing.html"
