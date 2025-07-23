from drf_yasg.utils import swagger_auto_schema
from ticket_project import swagger_service
from django.urls import path, include
from ticket_app.views import FetchTicketDetails, CreateTicketDetails, UpdateTicketDetails, DeleteTicketDetails, \
    SearchTicketDetails

urlpatterns = [
    # Swagger docs
    path('docs/', swagger_service.schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    path('Ticket_service/', include([
        path('', include([
            path('create_customer_ticket/', CreateTicketDetails.as_view()),
            path('get_customer_ticket/<int:customer_id>/', FetchTicketDetails.as_view()),
            # path('get_customer_ticket', FetchTicketDetails.as_view()),
            path('update_customer_ticket/', UpdateTicketDetails.as_view()),
            path('search_customer_ticket/', SearchTicketDetails.as_view()),
            path('delete_customer_ticket/', DeleteTicketDetails.as_view()),
        ]))
    ])),

]
