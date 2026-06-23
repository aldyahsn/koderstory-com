---
name: wagtail-section-design-system
description: Use when creating or updating pages in the Wagtail section design system from a brief, screenshot, image, section list, or section/layout map. Guides Codex to map user intent to existing page sections, layout variants, component content, and section settings, then review the plan with the user before applying changes.
metadata:
  short-description: Build Wagtail pages from section variants
---

# Wagtail Section Design System

Use this skill when the user wants to create or update a Wagtail page using the existing section-based design system. The user may provide a page goal, screenshot, rough instructions, a list of sections, or a full section/variant map.

## Core Rule

Reuse the existing section models, templates, components, and layout variants first. Do not invent new templates, fields, or abstractions unless the requested page cannot be represented by the current system and the user confirms the new surface.

## First Inspect The Project

Before planning or editing, inspect the local project because variants and fields may change:

- `home/models.py` for section fields, layout constants, and relationships.
- `home/templates/home/sections/**` for available section templates.
- `home/templates/home/components/**` for reusable content partials.
- `config/static/css/config.css` for classes and theme variable behavior.
- `config/static/admin/css/section-editor.css` and `config/static/admin/js/section-editor.js` for Wagtail admin grouping, collapse behavior, and input layout conventions.
- Existing page data when modifying a page.

Prefer `rg` and focused `sed` reads.

## Input Handling

Accept any understandable input:

- Plain brief: "Create a landing page for an accounting app."
- Section list: "Hero, clients, features, CTA."
- Section map: "Hero half media right, clients centered heading row."
- Screenshot or image reference.
- Existing copy, rough notes, competitor inspiration, or mixed notes.

If the request is understandable but incomplete, infer conservative defaults from the codebase and current site. Ask concise clarification questions only when a missing choice would materially change the page, content, data model, or media usage.

## Existing Homepage Sections And Variants

Verify these against the code before using them.

Hero:

- `centered_simple`
- `split_media_right`
- `background_media`
- `centered_media_below`
- `half_media_right`
- `angled_media_right`

Clients:

- `centered_heading_row`
- `left_heading_row`
- `bordered_grid`
- `split_copy_grid`
- `row_cta`

Features:

- `list_media_right`
- `centered_two_column`
- `media_grid`
- `heading_media_below`
- `centered_three_column`
- `media_left_list`
- `card_columns`
- `split_media_list`
- `split_media_testimonial`
- `heading_left_grid`
- `intro_checklist`
- `feature_grid`

CTA:

- `left_stack`
- `centered`
- `horizontal_split`
- `media_left`

## Variant Selection Heuristics

If the user gives only a page goal, usually plan:

1. Hero
2. Clients/trust, when relevant
3. Features
4. CTA

Choose variants based on content:

- Use media-right hero variants when there is a product screenshot, app UI, device mockup, or strong image.
- Use centered hero variants for simple brochure or announcement pages.
- Use `background_media` only when the image is decorative enough to sit behind readable text.
- Use `centered_heading_row` for logo-only trust sections.
- Use `bordered_grid` when logos need a stronger visual container.
- Use `split_copy_grid` when the clients section needs explanatory copy or buttons.
- Use `row_cta` when logos lead into a short inline call to action.
- Use feature grids/cards for many independent features.
- Use feature media/list variants when one image supports the feature story.
- Use `intro_checklist` for process, benefits, or checklist-style value props.
- Use `split_media_testimonial` when social proof is central.
- Use centered CTA for short closing conversion.
- Use horizontal split or media-left CTA when CTA needs visual weight or supporting media.

## Required Review Before Applying

Before modifying files or page data, present a review plan and wait for explicit user approval.

The review must include:

- Page purpose and audience.
- Section order.
- Chosen variant for each section.
- Generated content summary for each section.
- Section settings for each section:
  - `enabled`
  - `layout`
  - `anchor_id`
  - `section_height`
  - `content_width`
  - `text_alignment`
  - `vertical_alignment`
  - color theme behavior: explicit theme or inherit global/default
- Media plan:
  - provided image
  - existing media
  - generated asset
  - placeholder
  - no image
- Any assumptions that affect content, layout, or implementation.

Do not apply changes until the user confirms the plan.

## Content Generation

Generate production-ready content, not lorem ipsum, unless the user asks for placeholders.

For each section, fill the relevant model fields:

- titles/headlines
- descriptions/body copy
- eyebrow/announcement text
- primary and secondary button labels/URLs
- client names/logos when needed
- feature titles/descriptions/links
- testimonial text/person data when needed
- image alt text for every image

Keep copy consistent with the existing site voice and avoid overlong text that will break compact layouts.

For newly created pages only, fill every enabled section with content-ready initial seed data. Do not leave rendered fields empty: titles, descriptions, buttons, feature rows, client rows, alt text, and CTA fields should be populated when the selected layout uses them. For existing pages, preserve current content unless the user explicitly asks to replace or regenerate it.

## Admin UI Consistency

All new page, section, global setting, navbar, and footer editor UI must follow the existing `ks-*` admin grouping style. Related fields should appear inside bordered group panels, and inputs inside each group must use an intentional row or grid layout with consistent widths.

Use `ks-component-group` for section content groups, `ks-section-settings` for per-section settings, `ks-global-settings-group` for global settings, `ks-navbar-settings-group` for navbar settings, and `ks-footer-settings-group` for footer settings. Use `ks-global-color-group` and `ks-color-row` for color picker groups.

Do not leave component inputs with random default Wagtail widths. Use full-width layout for rich text, chooser panels, inline panels, and long copy; use two-column or three-column rows for short settings such as label/URL pairs, spacing, alignment, dimensions, and colors.

For layout-controlled page components, include `data-section` and `data-component` attrs so `section-editor.js` can show and hide groups. Backend section/component groups should be collapsed by default when supported by the current Wagtail panel API or local admin JavaScript/CSS.

## Color Theme Rules

Default behavior:

- Leave section theme fields blank so sections inherit the site/global/default theme.
- Use explicit section themes only when the user asks for different visual treatments per section.
- If a section appears unthemed, verify both template style hooks and global/default theme fallback before changing individual layouts.

Every section variant should render the relevant `page.<section>_style` on its root section or equivalent root wrapper. If a layout uses a custom root class instead of `ks-section`, ensure CSS consumes the same theme variables.

## Media Rules

If the user provides an image or screenshot:

- Use it as a source for content/layout interpretation when requested.
- Use it directly only when it is suitable for the target section.
- Ask before replacing existing production media if the target is ambiguous.

If media is required but not provided, either use existing site media when appropriate or ask for the asset. Do not invent image file references.

## Apply Changes

After approval:

1. Update existing page fields and related objects using the current model structure.
2. Reuse existing templates and components.
3. Add migrations only if model/schema changes are truly required.
4. Avoid unrelated refactors.
5. Preserve user edits in the working tree.

## Validation

Run the cheapest relevant checks:

- `manage.py check` for Django/Wagtail changes.
- `makemigrations --check --dry-run` if model changes were not intended.
- Render or inspect page output when practical.

Report what changed, what was verified, and any remaining assumptions.
