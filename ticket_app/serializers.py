from rest_framework import serializers
from ticket_app import models


class CreateCustomerTicketSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    class Meta:
        model = models.CustomerSupportTickets
        fields = '__all__'



class FetchCustomerTicketSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

class SearchDetailsSerializer(serializers.Serializer):
    search_query = serializers.CharField(required=False)
    filter_queries = serializers.JSONField(required=False)
    offset = serializers.IntegerField(required=False)
    limits = serializers.IntegerField(required=False)



class FetchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerSupportTickets
        fields = "__all__"



class UpdateTicketSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    class Meta:
        model = models.CustomerSupportTickets
        fields = '__all__'

