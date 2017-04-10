# -*- coding: utf-8 -*-

"""
    mundiapilib.models.create_usage_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapilib.api_helper import APIHelper

class CreateUsageRequest(object):

    """Implementation of the 'CreateUsageRequest' model.

    Request for creating a usage

    Attributes:
        quantity (int): TODO: type description here.
        description (string): TODO: type description here.
        used_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity" : "quantity",
        "description" : "description",
        "used_at" : "used_at"
    }

    def __init__(self,
                 quantity=None,
                 description=None,
                 used_at=None):
        """Constructor for the CreateUsageRequest class"""

        # Initialize members of the class
        self.quantity = quantity
        self.description = description
        self.used_at = APIHelper.RFC3339DateTime(used_at) if used_at else None


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
        quantity = dictionary.get("quantity")
        description = dictionary.get("description")
        used_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("used_at")).datetime if dictionary.get("used_at") else None

        # Return an object of this model
        return cls(quantity,
                   description,
                   used_at)


