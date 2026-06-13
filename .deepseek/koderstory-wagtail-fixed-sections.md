# Koderstory Wagtail Fixed Sections Standard

Use this instruction when working on Koderstory Wagtail page models, editor panels, templates, or admin CSS.

## Main Rule

Koderstory pages use fixed named sections, not a fully free-form StreamField builder by default.

- Different page types can have different fixed sections.
- The editor should feel like a builder, but the page structure remains controlled.
- Content editing and section settings must be separated.

## Page Editor Tabs

Every fixed-section page should use:

- `Content`: text, images, buttons, cards, logos, repeated content.
- `Section settings`: activation toggles, layout, alignment, spacing, anchors, advanced settings.
- `Promote`: Wagtail native SEO/promote fields.
- `Settings`: Wagtail native page settings.

Use Wagtail native `TabbedInterface` and `ObjectList`.

## Section Activation

Every section should have an enable field:

- Field name: `{section}_enabled`
- Default: `True`
- Label: `Enable {section} section`
- Help text: `Show or hide the {section} section without deleting its content.`

Templates must wrap each public section with its enable field.

## Standard Section Settings

Every section may use these standard advanced settings:

- `{section}_section_height`
- `{section}_content_width`
- `{section}_text_alignment`
- `{section}_content_vertical_alignment`
- `{section}_content_horizontal_alignment`

Use shared choice lists where possible.

## Settings Panel Shape

Prefer one outer collapsible-looking `MultiFieldPanel` per section:

- `Hero settings`
- `Client logo settings`
- `Services settings`
- `Products settings`
- `CTA settings`

Inside each outer section settings panel, use two inner visual groups:

- `Settings`
- `Advanced`

Apply compact grid styling to the inner groups only. Do not make `Settings` and `Advanced` separate top-level section panels unless explicitly requested.

## Content Tab Rule

Keep these in `Content`:

- headings
- body text
- images
- alt text
- button labels and URLs
- cards and repeated items

Keep these in `Section settings`:

- enable/disable toggles
- layout
- image position
- heading category
- text font size
- button style
- animation
- anchor id
- section height
- content width
- alignment controls

## Admin CSS

- Use admin-only CSS through Wagtail hooks.
- Scope editor CSS with `data-ks-panel`.
- Use compact grids for inner settings groups.
- Keep input/select widths consistent.
- Bump CSS query string after admin CSS changes.

## Verification

Run:

```bash
../.venv/bin/python manage.py check
../.venv/bin/python manage.py makemigrations --check --dry-run
../.venv/bin/python manage.py test
```

Apply migrations only when new model fields were intentionally added:

```bash
../.venv/bin/python manage.py migrate
```
