# -*- coding: utf-8 -*-

"""
    mundiapi.models.get_location_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class GetLocationResponse(object):

    """Implementation of the 'GetLocationResponse' model.

    Response object for geetting an order location request

    Attributes:
        latitude (string): Latitude
        longitude (string): Longitude

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latitude" : "latitude",
        "longitude" : "longitude"
    }

    def __init__(self,
                 latitude=None,
                 longitude=None):
        """Constructor for the GetLocationResponse class"""

        # Initialize members of the class
        self.latitude = latitude
        self.longitude = longitude


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
        latitude = dictionary.get("latitude")
        longitude = dictionary.get("longitude")

        # Return an object of this model
        return cls(latitude,
                   longitude)


