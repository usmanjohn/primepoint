from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class CanonicalHostMiddleware:
    """Send the bare apex to the canonical www host, in one hop.

    The site is served at https://www.powerty.uz. The apex powerty.uz is an
    alias: whoever owns it must answer on https and redirect here, or every
    page exists at two URLs and Google splits the ranking between them.

    Only the hosts named in CANONICAL_HOST_ALIASES are redirected — never a
    blanket "anything that isn't canonical". Railway's healthcheck and the
    *.up.railway.app domain use their own Host headers, and a greedy rule
    (Django's own PREPEND_WWW is one) would bounce them to a host that does
    not exist. The default list holds the apex and nothing else, so this
    middleware is inert in development.

    It runs first in the stack so an http://powerty.uz/x request takes a
    single 301 to https://www.powerty.uz/x, rather than one hop to https on
    the wrong host from SecurityMiddleware and a second one to here.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        canonical = getattr(settings, 'CANONICAL_HOST', '')
        aliases = getattr(settings, 'CANONICAL_HOST_ALIASES', ())
        if canonical and request.get_host().split(':')[0] in aliases:
            target = f'https://{canonical}{request.get_full_path()}'
            return HttpResponsePermanentRedirect(target)
        return self.get_response(request)
