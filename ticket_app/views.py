import logging
from datetime import datetime, time, timedelta
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response
from ticket_app import models
from ticket_app import serializers
from ticket_app.utils.response_optimizer import ResponseGenerator


_logger = logging.getLogger(__name__)


class CreateTicketDetails(CreateAPIView):
    """This API class is used to create ticket  details"""
    serializer_class = serializers.CreateCustomerTicketSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer_class = serializers.CreateCustomerTicketSerializer(data=request.data)
            if serializer_class.is_valid(raise_exception=True):
                serializer_class.save()
                return Response(
                    ResponseGenerator(
                        200,
                        "Customer Ticket Details Information Created successfully",
                        "Customer Ticket Details Information were created successfully.",
                        serializer_class.data,
                    ).success_response()
                )
        except Exception as e:
            return Response(
                ResponseGenerator(
                    500,
                    "Customer Ticket  Details creating process is failed",
                    f"Customer Ticket Details creating process is failed due to {str(e)}",
                    {},
                    str(e),
                ).failed_response()
            )


class FetchTicketDetails(GenericAPIView):
    """This API is used to Fetch Ticket Details by Customer_id"""

    serializer_class = serializers.FetchCustomerTicketSerializer

    # def post(self, request, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        try:
            data = kwargs['customer_id']
            query = models.CustomerSupportTickets.objects.filter(customer_id = data)
            if not query.exists():
                return Response(
                    ResponseGenerator(
                        404,
                        "There is no Customer with this customer_id",
                        f"No tickets found for customer_id {data}",
                        [],
                    ).warning_response()
                )
            serializer_class = serializers.FetchDetailsSerializer(query, many=True)
            return Response(
                ResponseGenerator(
                    200,
                    "Customer Ticket Details  Fetched successfully",
                    "Customer Ticket Details  were found successfully.",
                    serializer_class.data,
                ).success_response()
            )
        except Exception as e:
            return Response(
                ResponseGenerator(
                    500,
                    "Customer Ticket  Details retrieval process is failed",
                    f"Customer Ticket Details retrieval process is failed due to {str(e)}",
                    {},
                    str(e),
                ).failed_response()
            )

class UpdateTicketDetails(UpdateAPIView):
    """This API is used to update ticket  details"""
    serializer_class = serializers.UpdateTicketSerializer

    def put(self, request, *args, **kwargs):
        try:
            user_update = models.CustomerSupportTickets.objects.get(customer_id=request.data['customer_id'])
            serializer_class = serializers.UpdateTicketSerializer(instance=user_update, data=request.data)
            if serializer_class.is_valid(raise_exception=True):
                self.perform_update(serializer_class)
                return Response(ResponseGenerator(200, "ticket details updated successfully",
                                                  "ticket details updated successfully",
                                                  serializer_class.data,
                                                  None).success_response())
            else:
                return Response(ResponseGenerator(400, "customer_id is not found",
                                                  "Ensure the customer_id is correct and try again", {},
                                                  ).warning_response())
        except Exception as e:
            return Response(ResponseGenerator(500, "ticket details updating process is failed",
                                              f"ticket details updating process is failed, due to {str(e)}", {},
                                              error_details=str(e)).failed_response())


class DeleteTicketDetails(GenericAPIView):
    """This API is used to delete ticket information"""
    serializer_class = serializers.FetchCustomerTicketSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        try:
            data = request.data["customer_id"]
            delete_records,_ = models.CustomerSupportTickets.objects.filter(customer_id=data).delete()
            if delete_records > 0:
                return Response(ResponseGenerator(200, "Ticket details deleted successfully",
                                                  "Ticket details deleted successfully",
                                                  [],
                                                  None).success_response())
            else:
                return Response(ResponseGenerator(400, "customer_id is not found",
                                                  "Ensure the customer_id is correct and try again", {},
                                                  ).warning_response())
        except Exception as e:
            return Response(ResponseGenerator(500, "Ticket details deleting process is failed",
                                              f"Ticket details deleting process is failed, due to {str(e)}", {},
                                              error_details=str(e)).failed_response())



class SearchTicketDetails(GenericAPIView):
    """This API is used to Search the Ticket Details by search and filter"""

    serializer_class = serializers.SearchDetailsSerializer

    # def post(self, request, *args, **kwargs):
    def post(self, request, *args, **kwargs):
        try:
            search_query = request.data.get("search_query")
            filter_queries = request.data.get("filter_queries")
            offset = request.data.get("offset", 0)
            limits = request.data.get("limits")
            if search_query:
               # search by name,email and description
               query = models.CustomerSupportTickets.objects.filter(
                   Q(customer_name__icontains=search_query) |
                   Q(email__icontains=search_query) |
                   Q(issue_description__icontains=search_query)
                   )
                # filter by status, priority and date range
            if filter_queries:
                status = filter_queries.get("status")
                priority = filter_queries.get("priority")
                start_date = filter_queries.get("start_time")
                end_date = filter_queries.get("end_time")

                if status and priority:
                    query = query.filter(status=status, priority=priority)
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

                    # Apply date filtering
                    query = query.filter(created_at__date__range=[start_date, end_date])
            if limits:
                limits = int(limits)
                query = query[offset:offset + limits]
            else:
                query = query[offset:]

            serializer_class = serializers.FetchDetailsSerializer(query, many=True)
            return Response(
                ResponseGenerator(
                    200,
                    "Customer Ticket Details  Fetched successfully",
                    "Customer Ticket Details  were found successfully.",
                    serializer_class.data,
                ).success_response()
            )
        except Exception as e:
            return Response(
                ResponseGenerator(
                    500,
                    "Customer Ticket  Details retrieval process is failed",
                    f"Customer Ticket Details retrieval process is failed due to {str(e)}",
                    {},
                    str(e),
                ).failed_response()
            )


