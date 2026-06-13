from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks


@hooks.register("insert_global_admin_css")
def builder_editor_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}?v=section-settings-4">',
        static("admin/css/builder-editor.css"),
    )
