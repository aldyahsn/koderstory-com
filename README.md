# koderstory_com

Wagtail + Tailwind website-builder foundation for company-owned multisite use.

## Current Direction

- Wagtail multisite, one admin, one codebase.
- Curated StreamField block library with variants.
- Site-specific global design settings for colors, fonts, buttons, images, favicon, cookies, themes, and advanced settings.
- Smart image fallbacks: required image variants validate, optional image variants can use local branded placeholders.
- Native Wagtail preview for v1.

## Local Development

```bash
.venv/bin/python manage.py migrate
.venv/bin/python manage.py createsuperuser
.venv/bin/python manage.py runserver 127.0.0.1:8000
```

Open:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Frontend

The committed `static/css/site.css` provides a working tokenized base. Tailwind is configured for future builds:

```bash
npm install
npm run build
```

## Verification

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py test
```
