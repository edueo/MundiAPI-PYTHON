# -*- coding: utf-8 -*-

"""
    mundiapilib.models.paging_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class PagingResponse(object):

    """Implementation of the 'PagingResponse' model.

    Object used for returning lists of objects with pagination

    Attributes:
        total (int): Total number of pages
        previous (string): Previous page
        next (string): Next page

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total" : "total",
        "previous" : "previous",
        "next" : "next"
    }

    def __init__(self,
                 total=None,
                 previous=None,
                 next=None):
        """Constructor for the PagingResponse class"""

        # Initialize members of the class
        self.total = total
        self.previous = previous
        self.next = next


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
        total = dictionary.get("total")
        previous = dictionary.get("previous")
        next = dictionary.get("next")

        # Return an object of this model
        return cls(total,
                   previous,
                   next)


