"""Every visitor is the same read-only guest — there are no accounts in the demo."""


class GuestUser:
    id = 1
    pk = 1
    username = 'guest'
    is_authenticated = True
    is_anonymous = False
    is_staff = False
    is_superuser = False
    is_active = True


GUEST = GuestUser()


class GuestUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = GUEST
        return self.get_response(request)


def user(request):
    return {'user': GUEST}
