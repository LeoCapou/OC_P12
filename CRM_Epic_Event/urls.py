from django.urls import path, include
from django.contrib import admin

from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from CRM.views import (
    ClientViewset,
    SalesContactViewSet,
    SupportContactViewSet,
    ContratViewset,
    EventViewset,
)

# routeur
router = routers.DefaultRouter()

router.register(r"clients", ClientViewset, basename="clients")
## generates:
# /clients/
# /clients/{pk}/

router.register(r"sales_contact", SalesContactViewSet, basename="sales_contact")
## generates:
# /sales_contact/
# /sales_contact/{pk}/

router.register(r"support_contact", SupportContactViewSet, basename="support_contact")
## generates:
# /support_contact/
# /support_contact/{pk}/

router.register(r"contrat", ContratViewset, basename="contrat")
## generates:
# /contrat/
# /contrat/{pk}/

router.register(r"event", EventViewset, basename="event")
## generates:
# /event/
# /event/{pk}/


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
