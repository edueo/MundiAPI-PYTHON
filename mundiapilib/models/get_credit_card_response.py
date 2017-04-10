# -*- coding: utf-8 -*-

"""
    mundiapilib.models.get_credit_card_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapilib.api_helper import APIHelper
import mundiapilib.models.get_billing_address_response
import mundiapilib.models.get_customer_response

class GetCreditCardResponse(object):

    """Implementation of the 'GetCreditCardResponse' model.

    Response object for getting a credit card

    Attributes:
        id (string): TODO: type description here.
        last_four_digits (string): TODO: type description here.
        brand (string): TODO: type description here.
        holder_name (string): TODO: type description here.
        exp_month (int): TODO: type description here.
        exp_year (int): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        billing_address (GetBillingAddressResponse): TODO: type description
            here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id" : "id",
        "last_four_digits" : "last_four_digits",
        "brand" : "brand",
        "holder_name" : "holder_name",
        "exp_month" : "exp_month",
        "exp_year" : "exp_year",
        "status" : "status",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "billing_address" : "billing_address",
        "customer" : "customer",
        "metadata" : "metadata",
        "deleted_at" : "deleted_at"
    }

    def __init__(self,
                 id=None,
                 last_four_digits=None,
                 brand=None,
                 holder_name=None,
                 exp_month=None,
                 exp_year=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 billing_address=None,
                 customer=None,
                 metadata=None,
                 deleted_at=None):
        """Constructor for the GetCreditCardResponse class"""

        # Initialize members of the class
        self.id = id
        self.last_four_digits = last_four_digits
        self.brand = brand
        self.holder_name = holder_name
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.billing_address = billing_address
        self.customer = customer
        self.metadata = metadata
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id")
        last_four_digits = dictionary.get("last_four_digits")
        brand = dictionary.get("brand")
        holder_name = dictionary.get("holder_name")
        exp_month = dictionary.get("exp_month")
        exp_year = dictionary.get("exp_year")
        status = dictionary.get("status")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        billing_address = mundiapilib.models.get_billing_address_response.GetBillingAddressResponse.from_dictionary(dictionary.get("billing_address")) if dictionary.get("billing_address") else None
        customer = mundiapilib.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get("customer")) if dictionary.get("customer") else None
        metadata = dictionary.get("metadata")
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None

        # Return an object of this model
        return cls(id,
                   last_four_digits,
                   brand,
                   holder_name,
                   exp_month,
                   exp_year,
                   status,
                   created_at,
                   updated_at,
                   billing_address,
                   customer,
                   metadata,
                   deleted_at)


