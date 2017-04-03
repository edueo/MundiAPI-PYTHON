# -*- coding: utf-8 -*-

"""
    mundiapilib.models.create_cancel_subscription_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateCancelSubscriptionRequest():

    """Implementation of the 'CreateCancelSubscriptionRequest' model.

    Request for canceling a subscription

    Attributes:
        cancel_pending_invoices (bool): Indicates if the pending invoices must
            also be canceled.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancel_pending_invoices" : "cancel_pending_invoices"
    }

    def __init__(self,
                 cancel_pending_invoices=True):
        """Constructor for the CreateCancelSubscriptionRequest class"""

        # Initialize members of the class
        self.cancel_pending_invoices = cancel_pending_invoices


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
        cancel_pending_invoices = dictionary.get("cancel_pending_invoices") if dictionary.get("cancel_pending_invoices") else True
        # Return an object of this model
        return cls(cancel_pending_invoices)


