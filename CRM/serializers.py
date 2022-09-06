from rest_framework.serializers import ModelSerializer

from CRM.models import Client, Sales_Contact, Support_Contact, Contrat, Event


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class SalesContactSerializer(ModelSerializer):
    class Meta:
        model = Sales_Contact
        fields = "__all__"


class SupportContactSerializer(ModelSerializer):
    class Meta:
        model = Support_Contact
        fields = "__all__"


class ContratSerializer(ModelSerializer):
    class Meta:
        model = Contrat
        fields = "__all__"


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
