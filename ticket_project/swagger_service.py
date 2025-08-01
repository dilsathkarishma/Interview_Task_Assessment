from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Customer Ticket  API",
      default_version='v1',
      description="API to do the crud operations",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
