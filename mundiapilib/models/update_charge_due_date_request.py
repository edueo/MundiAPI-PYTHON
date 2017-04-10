# -*- coding: utf-8 -*-

"""
    mundiapilib.models.update_charge_due_date_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapilib.api_helper import APIHelper

class UpdateChargeDueDateRequest(object):

    """Implementation of the 'UpdateChargeDueDateRequest' model.

    Request for updating a charge due date

    Attributes:
        due_at (datetime): The charge's new due date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "due_at" : "due_at"
    }

    def __init__(self,
                 due_at=None):
        """Constructor for the UpdateChargeDueDateRequest class"""

        # Initialize members of the class
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None


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
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None

        # Return an object of this model
        return cls(due_at)


