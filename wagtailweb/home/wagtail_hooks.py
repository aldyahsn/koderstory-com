import json

from django.templatetags.static import static
from django.urls import path
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    BlockElementHandler,
)
from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from . import views
from .models import BlogIndexPage, HomePage, ServiceDetailPage, ServicePage


RICH_TEXT_ALIGNMENT_FEATURES = [
    {
        "name": "align-left",
        "block_type": "align-left",
        "css_class": "text-start",
        "icon": "align-left",
        "description": _("Align left"),
    },
    {
        "name": "align-center",
        "block_type": "align-center",
        "css_class": "text-center",
        "icon": "align-center",
        "description": _("Align center"),
    },
    {
        "name": "align-right",
        "block_type": "align-right",
        "css_class": "text-end",
        "icon": "align-right",
        "description": _("Align right"),
    },
]


@hooks.register("register_icons")
def register_alignment_icons(icons):
    return icons + [
        "home/icons/align-left.svg",
        "home/icons/align-center.svg",
        "home/icons/align-right.svg",
    ]


@hooks.register("register_rich_text_features")
def register_rich_text_alignment(features):
    for alignment in RICH_TEXT_ALIGNMENT_FEATURES:
        features.register_editor_plugin(
            "draftail",
            alignment["name"],
            draftail_features.BlockFeature(
                {
                    "type": alignment["block_type"],
                    "icon": alignment["icon"],
                    "description": alignment["description"],
                }
            ),
        )
        features.register_converter_rule(
            "contentstate",
            alignment["name"],
            {
                "from_database_format": {
                    f'p[class="{alignment["css_class"]}"]': BlockElementHandler(
                        alignment["block_type"]
                    ),
                },
                "to_database_format": {
                    "block_map": {
                        alignment["block_type"]: {
                            "element": "p",
                            "props": {"class": alignment["css_class"]},
                        }
                    }
                },
            },
        )


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}?v=14">'
        '<link rel="stylesheet" href="{}?v=1">',
        static("admin/css/section-editor.css"),
        static("admin/css/reset-settings.css"),
    )


@hooks.register("insert_global_admin_js")
def global_admin_js():
    variants = {
        "hero": {
            key: value["components"] for key, value in HomePage.HERO_VARIANTS.items()
        },
        "clients": {
            key: value["components"]
            for key, value in HomePage.CLIENTS_VARIANTS.items()
        },
        "features": {
            key: value["components"]
            for key, value in HomePage.FEATURES_VARIANTS.items()
        },
        "cta": {
            key: value["components"] for key, value in HomePage.CTA_VARIANTS.items()
        },
        "header": {
            key: value["components"]
            for key, value in ServicePage.HEADER_VARIANTS.items()
        },
        "content": {
            key: value["components"]
            for key, value in ServicePage.CONTENT_VARIANTS.items()
        },
        "bento": {
            key: value["components"]
            for key, value in ServiceDetailPage.BENTO_VARIANTS.items()
        },
        "blog": {
            key: value["components"]
            for key, value in BlogIndexPage.BLOG_VARIANTS.items()
        },
        "services": {
            key: value["components"]
            for key, value in ServicePage.SERVICES_VARIANTS.items()
        },
    }
    return format_html(
        '<script>window.KS_SECTION_VARIANTS = {};</script>'
        '<script src="{}?v=5"></script>'
        '<script src="{}?v=1"></script>'
        '<script src="{}?v=1"></script>'
        '<script src="{}?v=1"></script>',
        mark_safe(json.dumps(variants)),
        static("admin/js/section-editor.js"),
        static("admin/js/reset-settings.js"),
        static("admin/js/set-default-theme.js"),
        static("admin/js/social-icon-variant.js"),
    )


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(
            "settings/home/designsystemsettings/reset/<int:site_pk>/",
            views.reset_settings,
            name="reset_global_settings",
        ),
        path(
            "snippets/home/colortheme/<int:theme_pk>/set-default/",
            views.set_theme_as_default,
            name="set_theme_as_default",
        ),
    ]
