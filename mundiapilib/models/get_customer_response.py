# -*- coding: utf-8 -*-

"""
    mundiapilib.models.get_customer_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapilib.api_helper import APIHelper
import mundiapilib.models.get_address_response

class GetCustomerResponse():

    """Implementation of the 'GetCustomerResponse' model.

    Response object for getting a customer

    Attributes:
        id (string): TODO: type description here.
        name (string): TODO: type description here.
        email (string): TODO: type description here.
        delinquent (bool): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        phone (string): TODO: type description here.
        document (string): TODO: type description here.
        person_type (string): TODO: type description here.
        fb_access_token (string): TODO: type description here.
        address (GetAddressResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        fb_id (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id" : "id",
        "name" : "name",
        "email" : "email",
        "delinquent" : "delinquent",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "phone" : "phone",
        "document" : "document",
        "person_type" : "person_type",
        "fb_access_token" : "fb_access_token",
        "address" : "address",
        "metadata" : "metadata",
        "fb_id" : "fb_id"
    }

    def __init__(self,
                 id=None,
                 name=None,
                 email=None,
                 delinquent=None,
                 created_at=None,
                 updated_at=None,
                 phone=None,
                 document=None,
                 person_type=None,
                 fb_access_token=None,
                 address=None,
                 metadata=None,
                 fb_id=None):
        """Constructor for the GetCustomerResponse class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.email = email
        self.delinquent = delinquent
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.phone = phone
        self.document = document
        self.person_type = person_type
        self.fb_access_token = fb_access_token
        self.address = address
        self.metadata = metadata
        self.fb_id = fb_id


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
        name = dictionary.get("name")
        email = dictionary.get("email")
        delinquent = dictionary.get("delinquent")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        phone = dictionary.get("phone")
        document = dictionary.get("document")
        person_type = dictionary.get("person_type")
        fb_access_token = dictionary.get("fb_access_token")
        address = mundiapilib.models.get_address_response.GetAddressResponse.from_dictionary(dictionary.get("address")) if dictionary.get("address") else None
        metadata = dictionary.get("metadata")
        fb_id = dictionary.get("fb_id")
        # Return an object of this model
        return cls(id,
                   name,
                   email,
                   delinquent,
                   created_at,
                   updated_at,
                   phone,
                   document,
                   person_type,
                   fb_access_token,
                   address,
                   metadata,
                   fb_id)


