# -*- coding: utf-8 -*-

"""
    mundiapilib.models.create_order_item_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateOrderItemRequest(object):

    """Implementation of the 'CreateOrderItemRequest' model.

    Request for creating an order item

    Attributes:
        amount (int): Amount
        description (string): Description
        quantity (int): Quantity

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount" : "amount",
        "description" : "description",
        "quantity" : "quantity"
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 quantity=None):
        """Constructor for the CreateOrderItemRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.description = description
        self.quantity = quantity


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
        description = dictionary.get("description")
        quantity = dictionary.get("quantity")

        # Return an object of this model
        return cls(amount,
                   description,
                   quantity)


