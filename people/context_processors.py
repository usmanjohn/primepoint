def notification_context(request):
    if not request.user.is_authenticated:
        return {'unread_notif_count': 0}
    from .models import Notification
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return {'unread_notif_count': count}
