# Taste (Continuously Learned by [CommandCode][cmd])

[cmd]: https://commandcode.ai/

# wagtail
See [wagtail/taste.md](wagtail/taste.md)

# icons
- For social media icons in the Wagtail project, use Tabler UI Icons (https://tabler.io/icons) instead of custom SVGs or Bootstrap icons. Confidence: 0.65
- When using Tabler icons, only show outline variant for platforms that don't have a filled variant in Tabler — don't create custom filled versions. Confidence: 0.87
- Remove unrecognized platforms from the icon set rather than using custom/fallback SVGs for platforms not in Tabler. Confidence: 0.85
