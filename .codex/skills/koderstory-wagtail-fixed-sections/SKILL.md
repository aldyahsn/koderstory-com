---
name: koderstory-wagtail-fixed-sections
description: Use when working on Koderstory Wagtail pages that use fixed page sections instead of a fully flexible StreamField builder. Follow this for page editor structure, content/settings separation, section activation toggles, and reusable section settings patterns.
---

# Koderstory Wagtail Fixed Sections

Use this skill when editing Koderstory Wagtail page models, panels, templates, or admin CSS for fixed-section pages.

## Core Pattern

- Pages use fixed, named sections rather than a free-form page builder.
- Different page types may have different fixed sections.
- Every page editor has a `Content` tab and a `Section settings` tab.
- `Content` is for editable content: text, images, buttons, cards, logos, and repeated content.
- `Section settings` is for behavior and presentation: enable/disable, layout, alignment, spacing, anchors, and advanced controls.
- Sections can be activated or disabled from `Section settings` without deleting content.

## Section Settings

Every section should have an enable toggle:

- `section_enabled`
- Default: `True`
- Label format: `Enable {section} section`
- Help text: `Show or hide the {section} section without deleting its content.`

Standard advanced settings:

- `section_height`
- `content_width`
- `text_alignment`
- `content_vertical_alignment`
- `content_horizontal_alignment`

Add section-specific settings only when relevant:

- Hero: layout, image position, heading category, text font size, button style, animation.
- Sections with buttons: button style.
- Text sections: heading category, text font size, animation.

## Wagtail Admin Panels

- Use Wagtail native page-level tabs with `TabbedInterface`.
- Use `ObjectList(content_panels, heading="Content")`.
- Use `ObjectList(section_settings_panels, heading="Section settings")`.
- Keep Wagtail native `Promote` and `Settings` tabs.
- Do not build custom block-level tabs unless explicitly requested.
- Use one outer collapsible `MultiFieldPanel` per section in `Section settings`, for example `Hero settings`.
- Inside that outer panel, use two inner visual groups: `Settings` and `Advanced`.
- Apply compact grid styling to the inner groups only, not the outer collapsible panel.
- Do not make `Settings` and `Advanced` separate top-level section panels unless the user asks.

## Admin Styling

- Use admin-only CSS loaded through `insert_global_admin_css`.
- Keep styles scoped with `data-ks-panel`.
- Use a compact grid for inner setting groups.
- Keep select/input widths consistent across settings panels.
- Bump the admin CSS query string when changing admin CSS.

## Frontend Behavior

- Templates must respect `section_enabled` fields.
- Disabled sections should not render public markup.
- Content should remain stored and editable while hidden.
- Avoid applying newly added visual settings to frontend output until the behavior is intentionally requested.

## Verification

Run from the active Wagtail project directory:

```bash
../.venv/bin/python manage.py check
../.venv/bin/python manage.py makemigrations --check --dry-run
../.venv/bin/python manage.py test
```

If migrations were created intentionally, apply them locally:

```bash
../.venv/bin/python manage.py migrate
```
