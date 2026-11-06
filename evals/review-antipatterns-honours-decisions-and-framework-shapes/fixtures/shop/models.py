"""Persistence model of an order."""

from django.db import models


class Order(models.Model):
    """One customer order, as stored. Read and written by the handlers."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
    ]

    customer_email = models.EmailField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    total_cents = models.IntegerField()
    currency = models.CharField(max_length=3)
    placed_at = models.DateTimeField(auto_now_add=True)

    def mark_paid(self):
        self.status = "paid"
        self.save(update_fields=["status"])

    def mark_shipped(self):
        self.status = "shipped"
        self.save(update_fields=["status"])
