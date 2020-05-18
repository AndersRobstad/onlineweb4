from rest_framework import mixins, permissions, viewsets

from apps.notifications.models import (
    Notification,
    NotificationSetting,
    NotificationSubscription,
)
from apps.notifications.serializers import (
    NotificationReadOnlySerializer,
    NotificationSettingSerializer,
    NotificationSubscriptionSerializer,
)


class NotificationSettingsViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationSettingSerializer

    def get_queryset(self):
        user = self.request.user
        settings = NotificationSetting.objects.filter(user=user)

        """ Make sure notification settings for all types exist for user """
        if settings.count() == 0:
            NotificationSetting.create_all_for_user(user)
            settings = NotificationSetting.objects.filter(user=user)

        return settings


class NotificationSubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationSubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        return NotificationSubscription.objects.filter(user=user)


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationReadOnlySerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)
