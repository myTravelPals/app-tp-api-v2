# django
from django.db import models


class ContactUsMessage(models.Model):
    class Meta:
        managed = False
        db_table = "client_messages_contactusmessage"

    GENERAL_INQUIRY = "GI"
    BUSINESS_INQUIRY = "BI"
    COLLABORATION_INQUIRY = "CI"

    INQUIRIES_CHOICES = [
        (GENERAL_INQUIRY, "General Inquiry"),
        (BUSINESS_INQUIRY, "Business Inquiry"),
        (COLLABORATION_INQUIRY, "Collaboration Inquiry"),
    ]

    STATUS_PENDING = "PE"
    STATUS_PROCESSING = "PR"
    STATUS_REJECTED = "RE"
    STATUS_COMPLETED = "CO"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_COMPLETED, "Completed"),
    ]

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        max_length=255
    )

    phone_number = models.CharField(
        max_length=50
    )

    subject_inquiry = models.CharField(
        max_length=2,
        choices=INQUIRIES_CHOICES,
        default=GENERAL_INQUIRY,
    )

    message = models.TextField(
        max_length=500
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    date_submitted = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.email}-{self.subject_inquiry}-{self.date_submitted}"


class ClientRegistration(models.Model):
    class Meta:
        managed = False
        db_table = 'newsletter_clientregistration'

    email = models.EmailField(
        max_length=255,
        unique=True
    )

    date_registered = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.email}"