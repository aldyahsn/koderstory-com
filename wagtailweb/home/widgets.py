from django.forms.widgets import Input


class ColorInputWidget(Input):
    input_type = "color"

    def __init__(self, attrs=None):
        default_attrs = {
            "style": "width: 3rem; height: 2.5rem; padding: 0.125rem; cursor: pointer;"
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
