# Taste (Continuously Learned by [CommandCode][cmd])

[cmd]: https://commandcode.ai/

# wagtail
- Button background color should reference the brand color field rather than using a hardcoded default hex. Confidence: 0.60
- Button style config (border, padding, colors) needs to be implemented across all section layout templates, not just base.html and CSS. Confidence: 0.60
- Remove the button_shape field — button shape should not be a separate configurable option. Confidence: 0.65
- When creating a new home page, populate sections with dummy/filler content so the user can visualize the template layout. Confidence: 0.80
- For vertical-axis properties like section height, use names that describe vertical dimension (e.g., compact, tall) rather than horizontal terms (e.g., narrow, wide). Confidence: 0.72

