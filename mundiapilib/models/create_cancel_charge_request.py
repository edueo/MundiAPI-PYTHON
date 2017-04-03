# -*- coding: utf-8 -*-

"""
    mundiapilib.models.create_cancel_charge_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateCancelChargeRequest():

    """Implementation of the 'CreateCancelChargeRequest' model.

    Request for canceling a charge.

    Attributes:
        amount (int): The amount that will be canceled.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount" : "amount"
    }

    def __init__(self,
                 amount=None):
        """Constructor for the CreateCancelChargeRequest class"""

        # Initialize members of the class
        self.amount = amount


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
        amount = dictionary.get("amount")
        # Return an object of this model
        return cls(amount)


