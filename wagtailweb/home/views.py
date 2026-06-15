from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _

from wagtail.admin import messages
from wagtail.models import Site

from .models import DesignSystemSettings


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
