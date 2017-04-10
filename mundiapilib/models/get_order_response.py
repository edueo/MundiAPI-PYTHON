# -*- coding: utf-8 -*-

"""
    mundiapilib.models.get_order_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapilib.api_helper import APIHelper
import mundiapilib.models.get_order_item_response
import mundiapilib.models.get_customer_response
import mundiapilib.models.get_charge_response
import mundiapilib.models.get_shipping_response

class GetOrderResponse(object):

    """Implementation of the 'GetOrderResponse' model.

    Response object for getting an Order

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        currency (string): TODO: type description here.
        items (list of GetOrderItemResponse): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        charge (GetChargeResponse): TODO: type description here.
        invoice_url (string): TODO: type description here.
        shipping (GetShippingResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id" : "id",
        "code" : "code",
        "currency" : "currency",
        "items" : "items",
        "customer" : "customer",
        "status" : "status",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "charge" : "charge",
        "invoice_url" : "invoice_url",
        "shipping" : "shipping",
        "metadata" : "metadata"
    }

    def __init__(self,
                 id=None,
                 code=None,
                 currency=None,
                 items=None,
                 customer=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 charge=None,
                 invoice_url=None,
                 shipping=None,
                 metadata=None):
        """Constructor for the GetOrderResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.currency = currency
        self.items = items
        self.customer = customer
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.charge = charge
        self.invoice_url = invoice_url
        self.shipping = shipping
        self.metadata = metadata


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
        code = dictionary.get("code")
        currency = dictionary.get("currency")
        items = None
        if dictionary.get("items") != None:
            items = list()
            for structure in dictionary.get("items"):
                items.append(mundiapilib.models.get_order_item_response.GetOrderItemResponse.from_dictionary(structure))
        customer = mundiapilib.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get("customer")) if dictionary.get("customer") else None
        status = dictionary.get("status")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        charge = mundiapilib.models.get_charge_response.GetChargeResponse.from_dictionary(dictionary.get("charge")) if dictionary.get("charge") else None
        invoice_url = dictionary.get("invoice_url")
        shipping = mundiapilib.models.get_shipping_response.GetShippingResponse.from_dictionary(dictionary.get("shipping")) if dictionary.get("shipping") else None
        metadata = dictionary.get("metadata")

        # Return an object of this model
        return cls(id,
                   code,
                   currency,
                   items,
                   customer,
                   status,
                   created_at,
                   updated_at,
                   charge,
                   invoice_url,
                   shipping,
                   metadata)


