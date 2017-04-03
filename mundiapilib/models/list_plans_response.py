# -*- coding: utf-8 -*-

"""
    mundiapilib.models.list_plans_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapilib.models.get_plan_response

class ListPlansResponse():

    """Implementation of the 'ListPlansResponse' model.

    Response object for listing plans

    Attributes:
        data (list of GetPlanResponse): The plan objects
        paging (string): Paging object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data" : "data",
        "paging" : "paging"
    }

    def __init__(self,
                 data=None,
                 paging=None):
        """Constructor for the ListPlansResponse class"""

        # Initialize members of the class
        self.data = data
        self.paging = paging


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
        data = None
        if dictionary.get("data") != None:
            data = list()
            for structure in dictionary.get("data"):
                data.append(mundiapilib.models.get_plan_response.GetPlanResponse.from_dictionary(structure))
        paging = dictionary.get("paging")
        # Return an object of this model
        return cls(data,
                   paging)


