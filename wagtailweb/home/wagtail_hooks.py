import json

from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail import hooks

from .models import HomePage


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("admin/css/section-editor.css?v=1"),
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
    }
    return format_html(
        '<script>window.KS_SECTION_VARIANTS = {};</script>'
        '<script src="{}"></script>',
        mark_safe(json.dumps(variants)),
        static("admin/js/section-editor.js?v=1"),
    )
