from django.forms.widgets import Input
from django.utils.html import format_html


class ColorInputWidget(Input):
    input_type = "text"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "ks-color-input__value",
            "placeholder": "#hex, rgb(), rgba()",
        }
        if attrs:
            if attrs.get("class"):
                attrs = {
                    **attrs,
                    "class": f"{default_attrs['class']} {attrs['class']}",
                }
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        html = super().render(name, value, attrs, renderer)
        input_id = attrs.get("id", "")
        color_value = value if isinstance(value, str) and value.startswith("#") else ""
        picker_value = color_value[:7] if len(color_value) >= 7 else "#ffffff"

        return format_html(
            '<div class="ks-color-input" data-ks-color-input>'
            '<input type="color" id="{}_picker" class="ks-color-input__picker" value="{}" aria-label="Choose color">'
            '<div class="ks-color-input__main">{}</div>'
            '<label class="ks-color-input__alpha">'
            '<span>Opacity</span>'
            '<input type="range" id="{}_alpha" class="ks-color-input__alpha-range" min="0" max="100" step="1" value="100">'
            '<output class="ks-color-input__alpha-output" for="{}_alpha">100%</output>'
            '</label>'
            "</div>",
            input_id,
            picker_value,
            html,
            input_id,
            input_id,
        )
