from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from CRM.models import Client, Sales_Contact, Support_Contact, Contrat, Event

from .permissions import (
    Access_Client,
    Access_Contrat,
    Access_Event,
)

from CRM.serializers import (
    ClientSerializer,
    SalesContactSerializer,
    SupportContactSerializer,
    ContratSerializer,
    EventSerializer,
)


class EventViewset(ModelViewSet):
    """
    EVENT
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated & Access_Event]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["date_created"]
    search_fields = ["contrat__client__last_name", "contrat__client__email"]

    def get_queryset(self):
        if "pk" in self.kwargs:
            return Event.objects.filter(pk=self.kwargs["pk"])
        else:
            return Event.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data.update(
                date_created=datetime.now(),
                date_updated=datetime.now(),
            )
            serializer = EventSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                event = self.perform_create(serializer)
                event = serializer.save()
                event.save()
                return Response(
                    {"Message": "Un event a été créé."},
                    status=status.HTTP_200_OK,
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"Message": "Quelque chose a échoué à cause de {}".format(str(e))},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        data = request.data.copy()
        data.update(
            date_updated=datetime.now(),
        )
        event_serializer = EventSerializer(event, data=data, partial=True)

        if event_serializer.is_valid():
            event_serializer.save()
            return Response(
                {"Message": "Le contrat a bien été modifié"}, status=status.HTTP_200_OK
            )

        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        event = self.get_object()
        event.delete()
        return Response(
            {"Message": "Le event a été supprimé."}, status=status.HTTP_200_OK
        )


class ContratViewset(ModelViewSet):
    """
    CONTRAT
    """

    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated & Access_Contrat]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["status"]
    ordering_fields = ["amount", "date_created"]
    search_fields = ["client__last_name", "client__email"]

    def get_queryset(self):
        if "pk" in self.kwargs:
            return Contrat.objects.filter(pk=self.kwargs["pk"])
        else:
            return Contrat.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data.update(
                date_created=datetime.now(),
                date_updated=datetime.now(),
            )
            serializer = ContratSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                contrat = self.perform_create(serializer)
                contrat = serializer.save()
                contrat.save()
                return Response(
                    {"Message": "Un contrat a été créé."},
                    status=status.HTTP_200_OK,
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"Message": "Quelque chose a échoué à cause de {}".format(str(e))},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        contrat = self.get_object()
        data = request.data.copy()
        data.update(
            date_updated=datetime.now(),
        )
        contrat_serializer = ContratSerializer(contrat, data=data, partial=True)

        if contrat_serializer.is_valid():
            contrat_serializer.save()
            return Response(
                {"Message": "Le contrat a bien été modifié"}, status=status.HTTP_200_OK
            )

        return Response(contrat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        contrat = self.get_object()
        contrat.delete()
        return Response(
            {"Message": "Le contrat a été supprimé."}, status=status.HTTP_200_OK
        )


class ClientViewset(ModelViewSet):
    """
    CLIENT
    """

    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated & Access_Client]

    filter_backends = [SearchFilter]
    search_fields = ["last_name", "email"]

    def get_queryset(self):
        if "pk" in self.kwargs:
            return Client.objects.filter(pk=self.kwargs["pk"])
        else:
            return Client.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data.update(
                date_created=datetime.now(),
                date_updated=datetime.now(),
            )
            serializer = ClientSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                client = self.perform_create(serializer)
                client = serializer.save()
                client.save()
                return Response(
                    {"Message": "Un client a été créé."},
                    status=status.HTTP_200_OK,
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"Message": "Quelque chose a échoué à cause de {}".format(str(e))},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        data = request.data.copy()
        data.update(
            date_updated=datetime.now(),
        )
        client_serializer = ClientSerializer(client, data=data, partial=True)

        if client_serializer.is_valid():
            client_serializer.save()
            return Response(
                {"Message": "Le client a bien été modifié"}, status=status.HTTP_200_OK
            )

        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.delete()
        return Response(
            {"Message": "Le client a été supprimé."}, status=status.HTTP_200_OK
        )


class SalesContactViewSet(ModelViewSet):
    """
    SALES CONTACT
    """

    serializer_class = SalesContactSerializer

    def get_queryset(self):
        if "pk" in self.kwargs:
            return Sales_Contact.objects.filter(pk=self.kwargs["pk"])
        else:
            return Sales_Contact.objects.all()

    def update(self, request, *args, **kwargs):
        sales_contact = self.get_object()
        sales_contact_serializer = SalesContactSerializer(
            sales_contact, data=request.data, partial=True
        )

        if sales_contact_serializer.is_valid():
            sales_contact_serializer.save()
            return Response(
                {"Message": "Le Sales Contact a bien été modifié"},
                status=status.HTTP_200_OK,
            )

        return Response(
            sales_contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        sales_contact = self.get_object()
        sales_contact.delete()
        return Response(
            {"Message": "Le Sales Contact a été supprimé."}, status=status.HTTP_200_OK
        )


class SupportContactViewSet(ModelViewSet):
    """
    SUPPORT CONTACT
    """

    serializer_class = SupportContactSerializer

    def get_queryset(self):
        if "pk" in self.kwargs:
            return Support_Contact.objects.filter(pk=self.kwargs["pk"])
        else:
            return Support_Contact.objects.all()

    def update(self, request, *args, **kwargs):
        support_contact = self.get_object()
        support_contact_serializer = SupportContactSerializer(
            support_contact, data=request.data, partial=True
        )

        if support_contact_serializer.is_valid():
            support_contact_serializer.save()
            return Response(
                {"Message": "Le Support Contact a bien été modifié"},
                status=status.HTTP_200_OK,
            )

        return Response(
            support_contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        support_contact = self.get_object()
        support_contact.delete()
        return Response(
            {"Message": "Le Support Contact a été supprimé."}, status=status.HTTP_200_OK
        )
