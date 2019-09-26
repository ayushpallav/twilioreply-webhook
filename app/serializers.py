
from rest_framework import serializers


class  WebhookSerializer(serializers.Serializer):
	"""Serializer for payload coming from twilio"""
	from_cell = serializers.CharField()
	account_info = serializers.CharField()
	body = serializers.CharField()

	def create(self, validated_data):
		return validated_data
