from django.db import models


class CustomerSupportTickets(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    issue_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add= True)

    class Meta:
        managed = False
        db_table = 'customer_support_tickets'

