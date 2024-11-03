# django
from django.db import models

from api_auth.functions import create_api_token


class APIEndpoint(models.Model):
    class Meta:
        managed = False
        db_table = "api_auth_apiendpoint"

    name = models.CharField(
        max_length=255
    )

    url = models.CharField(
        max_length=255, unique=True
    )

    def __str__(self):
        return self.name


class APIKey(models.Model):
    class Meta:
        managed = False
        db_table = "api_auth_apikey"

    name = models.CharField(
        max_length=255
    )

    key = models.CharField(
        max_length=100,
        default=create_api_token,
        unique=True
    )

    api_endpoints = models.ManyToManyField(
        APIEndpoint
    )

    def __str__(self):
        return self.name
