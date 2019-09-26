
from rest_framework.generics import CreateAPIView

from app.serializers import WebhookSerializer


class WebhookView(CreateAPIView):
    """
    View to receive a post request payload from twilio
    and process it for other end points
    """

    serializer_class = WebhookSerializer
