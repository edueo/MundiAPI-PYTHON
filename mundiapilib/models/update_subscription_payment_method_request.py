# -*- coding: utf-8 -*-

"""
    mundiapilib.models.update_subscription_payment_method_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapilib.models.create_credit_card_request

class UpdateSubscriptionPaymentMethodRequest():

    """Implementation of the 'UpdateSubscriptionPaymentMethodRequest' model.

    Request for updating a subscription's payment method

    Attributes:
        payment_method (string): The new payment method
        credit_card_id (string): Credit card's id
        credit_card_gateway_id (string): Credit card's gateway id
        credit_card (CreateCreditCardRequest): Credit card data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_method" : "payment_method",
        "credit_card_id" : "credit_card_id",
        "credit_card_gateway_id" : "credit_card_gateway_id",
        "credit_card" : "credit_card"
    }

    def __init__(self,
                 payment_method=None,
                 credit_card_id=None,
                 credit_card_gateway_id=None,
                 credit_card=None):
        """Constructor for the UpdateSubscriptionPaymentMethodRequest class"""

        # Initialize members of the class
        self.payment_method = payment_method
        self.credit_card_id = credit_card_id
        self.credit_card_gateway_id = credit_card_gateway_id
        self.credit_card = credit_card


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
        payment_method = dictionary.get("payment_method")
        credit_card_id = dictionary.get("credit_card_id")
        credit_card_gateway_id = dictionary.get("credit_card_gateway_id")
        credit_card = mundiapilib.models.create_credit_card_request.CreateCreditCardRequest.from_dictionary(dictionary.get("credit_card")) if dictionary.get("credit_card") else None
        # Return an object of this model
        return cls(payment_method,
                   credit_card_id,
                   credit_card_gateway_id,
                   credit_card)


