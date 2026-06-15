from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _

from wagtail.admin import messages
from wagtail.models import Site

from .models import ColorTheme, DesignSystemSettings, HomePage


def reset_settings(request, site_pk):
    """Reset DesignSystemSettings to field defaults."""
    site = get_object_or_404(Site, pk=site_pk)
    setting = DesignSystemSettings.for_site(site)

    for field in setting._meta.fields:
        name = field.name
        if name in ("id", "site", "site_id"):
            continue
        setattr(setting, name, field.default)

    setting.save()

    messages.success(request, _("Global settings reset to defaults."))
    return redirect(
        "wagtailsettings:edit",
        "home",
        "designsystemsettings",
        site_pk,
    )


def set_theme_as_default(request, theme_pk):
    """Replace one theme with Default across all sections, skipping sections that use other themes."""
    theme = get_object_or_404(ColorTheme, pk=theme_pk)
    if theme_pk == 1:
        messages.warning(request, _("Default theme cannot be replaced."))
        return redirect("wagtailsnippets_home_colortheme:edit", theme_pk)

    # Clear previous default and set new one
    ColorTheme.objects.filter(is_default=True).update(is_default=False)
    ColorTheme.objects.filter(pk=theme_pk).update(is_default=True)

    fields = ["hero_theme", "clients_theme", "features_theme", "cta_theme"]
    fk_fields = [f.replace("_theme", "_theme_id") for f in fields]
    page_count = 0
    for page in HomePage.objects.all():
        has_match = False
        for fk in fk_fields:
            if getattr(page, fk) == int(theme_pk):
                setattr(page, fk, 1)
                has_match = True
        if has_match:
            page.save(update_fields=fk_fields)
            page_count += 1
    messages.success(
        request,
        _('All sections using "%(theme)s" have been reset to Default. (%(count)d pages updated)')
        % {"theme": theme.name, "count": page_count},
    )
    return redirect("wagtailsnippets_home_colortheme:edit", theme_pk)
