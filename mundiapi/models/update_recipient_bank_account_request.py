# -*- coding: utf-8 -*-

"""
    mundiapi.models.update_recipient_bank_account_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_bank_account_request

class UpdateRecipientBankAccountRequest(object):

    """Implementation of the 'UpdateRecipientBankAccountRequest' model.

    Updates the default bank account for a recipient

    Attributes:
        bank_account (CreateBankAccountRequest): Bank account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_account" : "bank_account"
    }

    def __init__(self,
                 bank_account=None):
        """Constructor for the UpdateRecipientBankAccountRequest class"""

        # Initialize members of the class
        self.bank_account = bank_account


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
        bank_account = mundiapi.models.create_bank_account_request.CreateBankAccountRequest.from_dictionary(dictionary.get("bank_account")) if dictionary.get("bank_account") else None

        # Return an object of this model
        return cls(bank_account)


