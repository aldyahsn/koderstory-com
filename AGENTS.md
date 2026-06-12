# koderstory_com Agent Notes

## Project Intent

Build a Wagtail + Tailwind website-builder foundation for company-owned multisite use.

The system should feel similar to a curated WP/Wix/Squarespace builder, but implemented with Wagtail page models, StreamField blocks, reusable variants, global design settings, and native Wagtail preview.

## Chosen Direction

- Use Wagtail multisite for related websites under one company.
- Use one Wagtail admin and one codebase.
- Keep content sharing explicit and controlled.
- Do not design v1 as full self-service SaaS.
- Do not use strict multi-instance isolation for v1.
- Use native Wagtail page preview in v1, not a full live visual editor.

## Builder Model

Use few block types with many visual variants.

Example:

- `HeroBlock`
  - `centered_simple`
  - `split_screenshot`
  - `dashboard_preview`
  - `image_background`
  - `announcement_centered`

Same content structure with different layout should be a variant, not a new block class.

Different content structure may become a separate block.

## Block Configuration Pattern

Each major block should have:

- Content fields
- CTA/button configuration
- Media/image fields
- Variant selector
- Safe settings
- Limited advanced settings

Advanced settings should use presets, not raw CSS.

Avoid exposing arbitrary styling controls that can break the design system.

## CTA Rules

Hero blocks should support up to 2 buttons:

- Primary CTA
- Secondary CTA

If a section needs many links, use a separate CTA group or link list block.

## Placeholder Rules

Do not use external placeholder services in production.

Use smart fallbacks:

- Required images should block publishing if missing.
- Optional images may hide the media area or use site-level fallback images.
- Use generated/local branded placeholders as the last fallback.

Site settings should include image-related global style:

- Default hero image
- Default blog/card placeholder
- Default avatar style
- Image radius
- Image border
- Image shadow
- Placeholder style

## Global Design Settings

Use site-specific settings for:

- Colors
- Fonts
- Buttons
- Favicon
- Cookie banner
- Themes
- Images/placeholders
- Advanced settings

Render these as CSS variables consumed by Tailwind/templates.

## Spacing And Tokens

Global tokens define margin, padding, container width, radius, grid gap, typography, color, and image style.

Components consume tokens. Blocks choose safe presets. Editors should not enter raw spacing values.

Example block settings:

- Section spacing: `default`, `compact`, `normal`, `spacious`
- Container width: `default`, `narrow`, `normal`, `wide`, `full`
- Color scheme: `white`, `light`, `dark`, `black`, `highlight`, `brand`
- Alignment: `left`, `center`

## Multisite Sharing Rules

Allowed to share intentionally:

- Block library
- Brand tokens
- Selected snippets
- Reusable media collections
- Authors/team profiles if intentional

Keep site-specific:

- Page tree
- Navigation
- Forms and submissions
- SEO metadata
- Redirects
- Analytics settings
- Homepage/content publishing

Nothing should appear across sites unless explicitly selected.

## Implementation Preference

Prefer clean Wagtail/Django conventions over custom framework behavior.

Keep editor experience curated, predictable, and hard to break.

## Current Implementation State

- Wagtail/Django project scaffold lives under `config/`.
- Reusable site-builder logic lives under `core/`.
- Page models live under `pages/`.
- Global design settings are implemented with `core.SiteDesignSettings`.
- StreamField blocks are implemented in `core.blocks`.
- Native Wagtail block previews are enabled through `templates/blocks/preview.html`.
- Public templates live under `templates/`.
- Tailwind source is `static/src/styles/app.css`; generated CSS is `static/css/site.css`.
- Local SQLite bootstrap migration creates a `localhost:8000` Wagtail Site and Home page.

## Verification Commands

Run these after changes:

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
.venv/bin/python manage.py test
npm run build
```

Run locally:

```bash
.venv/bin/python manage.py runserver 127.0.0.1:8000 --noreload
```
