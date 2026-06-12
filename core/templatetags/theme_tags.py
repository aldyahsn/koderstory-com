from urllib.parse import quote

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from core.tokens import CONTAINER_WIDTH_TOKENS, SECTION_SPACING_TOKENS, default_color_schemes


register = template.Library()


def _design_settings(context):
    request = context.get("request")
    if not request:
        return None
    try:
        from core.models import SiteDesignSettings

        return SiteDesignSettings.for_request(request)
    except Exception:
        return None


def _button_radius(shape):
    return {
        "square": "0rem",
        "soft": "0.5rem",
        "rounded": "0.875rem",
        "pill": "999px",
    }.get(shape, "0.5rem")


def _button_padding(value):
    return {
        "compact": ("0.625rem", "0.9rem"),
        "normal": ("0.75rem", "1.1rem"),
        "spacious": ("0.9rem", "1.35rem"),
    }.get(value, ("0.75rem", "1.1rem"))


def _image_radius(value):
    return {
        "none": "0rem",
        "sm": "0.375rem",
        "md": "0.75rem",
        "lg": "1rem",
    }.get(value, "0.75rem")


def _image_shadow(value):
    return {
        "none": "none",
        "soft": "0 16px 40px rgba(15, 23, 42, 0.10)",
        "medium": "0 24px 60px rgba(15, 23, 42, 0.16)",
        "strong": "0 32px 80px rgba(15, 23, 42, 0.24)",
    }.get(value, "0 16px 40px rgba(15, 23, 42, 0.10)")


@register.simple_tag(takes_context=True)
def site_design_css(context):
    settings = _design_settings(context)
    schemes = default_color_schemes()

    primary = "#4f46e5"
    accent = "#ecfe3a"
    background = "#ffffff"
    text = "#111827"
    heading_font = "Inter, ui-sans-serif, system-ui, sans-serif"
    body_font = heading_font
    button_font = heading_font
    button_radius = "0.5rem"
    button_border_width = 1
    button_padding_y = "0.75rem"
    button_padding_x = "1.1rem"
    image_radius = "0.75rem"
    image_shadow = "0 16px 40px rgba(15, 23, 42, 0.10)"
    custom_vars = ""

    if settings:
        schemes = settings.color_schemes or schemes
        primary = settings.primary_color
        accent = settings.accent_color
        background = settings.background_color
        text = settings.text_color
        heading_font = settings.heading_font
        body_font = settings.body_font
        button_font = settings.button_font
        button_radius = _button_radius(settings.button_shape)
        button_border_width = settings.button_border_width
        button_padding_y, button_padding_x = _button_padding(settings.button_padding)
        image_radius = _image_radius(settings.image_radius)
        image_shadow = _image_shadow(settings.image_shadow)
        custom_vars = settings.custom_css_variables

    css = [
        ":root {",
        f"  --color-primary: {primary};",
        f"  --color-accent: {accent};",
        f"  --color-background: {background};",
        f"  --color-text: {text};",
        f"  --font-heading: {heading_font};",
        f"  --font-body: {body_font};",
        f"  --font-button: {button_font};",
        f"  --radius-button: {button_radius};",
        f"  --button-border-width: {button_border_width}px;",
        f"  --button-padding-y: {button_padding_y};",
        f"  --button-padding-x: {button_padding_x};",
        f"  --radius-card: {image_radius};",
        f"  --image-shadow: {image_shadow};",
    ]

    for key, value in SECTION_SPACING_TOKENS.items():
        css.append(f"  --section-py-{key}: {value};")
    for key, value in CONTAINER_WIDTH_TOKENS.items():
        css.append(f"  --container-{key}: {value};")
    if custom_vars:
        css.append(custom_vars)
    css.append("}")

    for name, scheme in schemes.items():
        css.extend(
            [
                f".scheme-{name} {{",
                f"  --scheme-bg: {scheme.get('background', '#ffffff')};",
                f"  --scheme-border: {scheme.get('border', '#e5e7eb')};",
                f"  --scheme-heading: {scheme.get('heading', '#111827')};",
                f"  --scheme-text: {scheme.get('text', '#4b5563')};",
                f"  --scheme-link: {scheme.get('link', primary)};",
                "  --scheme-primary-button-bg: "
                f"{scheme.get('primary_button_background', primary)};",
                "  --scheme-primary-button-text: "
                f"{scheme.get('primary_button_text', '#ffffff')};",
                "  --scheme-primary-button-border: "
                f"{scheme.get('primary_button_border', primary)};",
                "  --scheme-secondary-button-bg: "
                f"{scheme.get('secondary_button_background', 'transparent')};",
                "  --scheme-secondary-button-text: "
                f"{scheme.get('secondary_button_text', '#111827')};",
                "  --scheme-secondary-button-border: "
                f"{scheme.get('secondary_button_border', '#d1d5db')};",
                "}",
            ]
        )

    return mark_safe("\n".join(css))


def _setting_value(settings, key, default):
    if not settings:
        return default
    try:
        value = settings.get(key)
    except AttributeError:
        value = getattr(settings, key, None)
    return value or default


@register.simple_tag
def section_classes(settings):
    scheme = _setting_value(settings, "color_scheme", "white")
    spacing = _setting_value(settings, "section_spacing", "normal")
    return f"site-section scheme-{scheme} section-spacing-{spacing}"


@register.simple_tag
def container_classes(settings):
    width = _setting_value(settings, "container_width", "normal")
    return f"site-container container-{width}"


@register.simple_tag
def alignment_class(settings):
    alignment = _setting_value(settings, "alignment", "left")
    return "text-center items-center" if alignment == "center" else "text-left items-start"


@register.simple_tag
def anchor_attr(settings):
    anchor = _setting_value(settings, "anchor_id", "")
    if not anchor:
        return ""
    return mark_safe(f'id="{conditional_escape(anchor)}"')


@register.simple_tag(takes_context=True)
def placeholder_data_uri(context, ratio="16x9", label="Image"):
    settings = _design_settings(context)
    primary = settings.primary_color if settings else "#4f46e5"
    accent = settings.accent_color if settings else "#ecfe3a"
    width, height = {
        "1x1": (800, 800),
        "4x3": (1200, 900),
        "3x2": (1200, 800),
        "16x9": (1600, 900),
        "16x10": (1600, 1000),
    }.get(ratio, (1600, 900))
    escaped_label = conditional_escape(label)
    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
      <defs>
        <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
          <stop offset="0%" stop-color="{primary}" stop-opacity="0.16"/>
          <stop offset="100%" stop-color="{accent}" stop-opacity="0.22"/>
        </linearGradient>
      </defs>
      <rect width="100%" height="100%" fill="#f8fafc"/>
      <rect x="0" y="0" width="100%" height="100%" fill="url(#g)"/>
      <rect x="{width * 0.08}" y="{height * 0.12}" width="{width * 0.84}" height="{height * 0.76}" rx="28" fill="#ffffff" fill-opacity="0.72" stroke="{primary}" stroke-opacity="0.24"/>
      <circle cx="{width * 0.5}" cy="{height * 0.42}" r="34" fill="{primary}" fill-opacity="0.85"/>
      <text x="50%" y="56%" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="42" fill="#111827">{escaped_label}</text>
    </svg>
    """
    return mark_safe(f"data:image/svg+xml,{quote(svg)}")


@register.simple_tag
def latest_blog_posts(limit=3):
    try:
        from pages.models import BlogPostPage

        return BlogPostPage.objects.live().public().order_by(
            "-date", "-first_published_at"
        )[:limit]
    except Exception:
        return []
