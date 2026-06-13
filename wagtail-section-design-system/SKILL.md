---
name: wagtail-section-design-system
description: Use when building or modifying Wagtail websites that use fixed page sections, global design settings, per-section settings tabs, variant layouts, and custom admin UI for a site-builder-like editor experience.
---

# Wagtail Section Design System

Use this skill for Wagtail sites where pages are composed from fixed named sections, not a fully flexible page builder.

## Core Behavior

- Prefer fixed page sections for client-editable marketing pages: hero, clients, services, products, CTA, FAQ, footer, etc.
- Put content fields in the page `Content` tab.
- Put presentation and behavior controls in a page-level `Section settings` tab.
- Each section has its own settings panel inside `Section settings`.
- Each section has an enable toggle so editors can hide it without deleting content.
- Each section can have a `layout` choice field that selects a template partial.
- A layout variant may use different components, but keep all section fields available in the page model unless there is a strong reason to split page types.
- Document each variant’s components and field usage in a Python map near the choices.
- Use admin-only CSS and Wagtail panels to make sections feel like a builder without replacing Wagtail.
- Keep frontend output template-driven: model chooses a template path, template renders the section.

## Ask First

Before creating a new page type or building a new group of sections, ask the user what page they want and what sections it contains unless the request already includes those details.

Ask for:

- Page type/name, for example `HomePage`, `LandingPage`, `ServicePage`, or `ProductPage`.
- Sections in page order.
- Section type for each section, for example `hero`, `clients`, `services`, `cta`, `faq`, `pricing`, `testimonials`, `contact`.
- Layout variants for each section.
- Layout-specific inputs/components, for example media, card list, logo list, quote, stats, buttons, form, or pricing plans.

Suggested intake format:

```text
Page: Home page
Sections:
- Hero: centered simple, split media right, angled image right
- Clients: heading top, simple row, dark grid
- Services: card grid, media right, dark media, checklist
- CTA: split, centered, bar, split media
```

If the user gives a section list with variants, use it as the source of truth. If details are missing, make the smallest reasonable assumption and state it before implementation.

## Global Design Settings

For site-wide variables, use Wagtail settings:

- Fonts: heading font, body font, font scale.
- Colors: brand, surface, text, muted text, accent.
- Spacing: section padding, container width, card radius, button radius.
- Output these as CSS custom properties in the base template or a generated design-token partial.

Use global settings for defaults. Use section settings only for section-specific overrides.

## Page Editor Pattern

Use page-level tabs:

- `Content`: title, text, media, buttons, cards, repeated content.
- `Section settings`: enable toggles, layout choices, alignment, spacing, anchors, advanced controls.
- `Promote`: Wagtail native.
- `Settings`: Wagtail native.

Inside `Section settings`, use one outer collapsible `MultiFieldPanel` per section, then two inner groups:

- `Settings`: common controls such as enabled, layout, image position, heading style, button style.
- `Advanced`: anchors, section height, content width, alignment, custom CSS class.

## Variant Map Pattern

Every section with variants should define:

- layout constants
- layout choices
- a variant map with template path, components, and fields used
- a `section_template_name` property

This lets the implementation understand which components belong to each layout while still keeping the editor stable.

Example variant metadata:

```python
HERO_VARIANTS = {
    HERO_LAYOUT_SPLIT_MEDIA: {
        "label": "Split media",
        "template": "home/includes/heroes/split_media.html",
        "components": ["eyebrow", "heading", "description", "buttons", "image"],
        "fields": [
            "hero_eyebrow",
            "hero_title",
            "hero_description",
            "hero_primary_button_label",
            "hero_image",
        ],
    },
}
```

## Admin UI

- Use `MultiFieldPanel`, `FieldRowPanel`, `InlinePanel`, `ObjectList`, and `TabbedInterface`.
- Add `classname` and `attrs={"data-ks-panel": "..."}` to panels for scoped styling.
- Load admin CSS with `insert_global_admin_css`.
- Keep admin CSS scoped to custom classes and `data-ks-panel`; avoid broad Wagtail admin overrides.
- Style section settings as bordered panels with compact grids.

For complete reusable snippets, read [references/wagtail-section-snippets.md](references/wagtail-section-snippets.md).

## Implementation Workflow

1. Clarify the page type, section list, section order, and layout variants if not already provided.
2. Read the existing Wagtail version, app structure, page model, templates, settings, and static setup.
3. Add or update global design settings first if the site needs design tokens.
4. For each page section, add content fields to `Content` and settings fields to `Section settings`.
5. Add layout choices and a variant map for sections with multiple layouts.
6. Move section rendering into include partials.
7. Add admin CSS only for editor usability.
8. Add migrations for model fields.
9. Add tests for renderability, disabled sections, layout switching, editor form fields, and global settings if used.

## Validation

Run from the Wagtail project directory:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

If migrations were intentionally created:

```bash
python manage.py migrate
```
