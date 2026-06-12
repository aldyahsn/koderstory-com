# Koderstory Bootstrap Simple UI

This version removes Tabler completely.

## Rules followed

- Bootstrap only
- No Tabler CSS
- No Tabler JS
- No Tabler Icons
- No dark mode
- No theme toggle
- No custom CSS file
- Simple background using Bootstrap utility classes only
- All image placeholders use:
  - https://placehold.net/600x600.png

## Notes

For rounded or circular image areas, the template still uses:
https://placehold.net/600x600.png

Then Bootstrap classes such as:
- rounded
- rounded-4
- rounded-circle

## Included pages

- index.html
- services.html
- service-web-app.html
- service-odoo-erp.html
- service-dashboard.html
- service-automation.html
- service-mobile-app.html
- products.html
- product-sirasa.html
- product-bimora.html
- industries.html
- work.html
- case-study-sirasa.html
- case-study-bimora.html
- case-study-odoo.html
- insights.html
- insight-detail.html
- about.html
- contact.html
- project-form.html
- thank-you.html
- privacy-policy.html
- cookie-policy.html
- terms.html


## Added typography customization

Custom typography files:

- `assets/css/custom.css`
- `assets/scss/custom.scss`

Typography rules:

- Heading font: Poppins
- Paragraph/body font: Nunito
- Maximum font weight: 400
- Maximum heading size: 48px
- No Tabler
- No dark mode
- Bootstrap only

Fonts are loaded from Google Fonts using only weight `400`.


## Added in v2

- Blog detail page updated to a Medium-like article layout:
  - centered article header
  - author row
  - large cover image
  - narrow readable content column
  - article body spacing
  - quote block
- Product key feature cards now include image placeholders.


## Added in v3

- Blog detail header changed to a jumbotron-style block.
- Removed duplicate image/card borders.
- Cards are now borderless through `assets/css/custom.css`.
- Kept Bootstrap only, no Tabler, no dark mode.


## Added in v4

- Removed the duplicated blog detail top header.
- Blog detail page now only shows the jumbotron-style header.
- Added Bootstrap breadcrumbs to child/detail pages:
  - service detail pages
  - product detail pages
  - case study pages
  - blog detail page
  - project form
  - thank-you page
  - legal pages
