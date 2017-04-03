# -*- coding: utf-8 -*-

"""
    mundiapilib.models.create_boleto_payment_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class CreateBoletoPaymentRequest():

    """Implementation of the 'CreateBoletoPaymentRequest' model.

    Contains the settings for creating a boleto payment

    Attributes:
        retries (int): Number of retries
        bank (string): The bank code, containing three characters. The
            available codes are on the API specification
        instructions (string): The instructions field that will be printed on
            the boleto.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "retries" : "retries",
        "bank" : "bank",
        "instructions" : "instructions"
    }

    def __init__(self,
                 retries=None,
                 bank=None,
                 instructions=None):
        """Constructor for the CreateBoletoPaymentRequest class"""

        # Initialize members of the class
        self.retries = retries
        self.bank = bank
        self.instructions = instructions


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
        retries = dictionary.get("retries")
        bank = dictionary.get("bank")
        instructions = dictionary.get("instructions")
        # Return an object of this model
        return cls(retries,
                   bank,
                   instructions)


