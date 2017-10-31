# -*- coding: utf-8 -*-

"""
    mundiapi.models.get_split_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.get_recipient_response

class GetSplitResponse(object):

    """Implementation of the 'GetSplitResponse' model.

    Split response

    Attributes:
        mtype (string): Type
        amount (int): Amount
        recipient (GetRecipientResponse): Recipient

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype" : "type",
        "amount" : "amount",
        "recipient" : "recipient"
    }

    def __init__(self,
                 mtype=None,
                 amount=None,
                 recipient=None):
        """Constructor for the GetSplitResponse class"""

        # Initialize members of the class
        self.mtype = mtype
        self.amount = amount
        self.recipient = recipient


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
        mtype = dictionary.get("type")
        amount = dictionary.get("amount")
        recipient = mundiapi.models.get_recipient_response.GetRecipientResponse.from_dictionary(dictionary.get("recipient")) if dictionary.get("recipient") else None

        # Return an object of this model
        return cls(mtype,
                   amount,
                   recipient)


