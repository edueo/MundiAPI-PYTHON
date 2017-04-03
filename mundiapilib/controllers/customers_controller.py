# -*- coding: utf-8 -*-

"""
    mundiapilib.controllers.customers_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.list_addresses_response import ListAddressesResponse
from ..models.list_cards_response import ListCardsResponse
from ..models.list_customers_response import ListCustomersResponse
from ..models.get_customer_response import GetCustomerResponse
from ..models.get_address_response import GetAddressResponse
from ..models.get_credit_card_response import GetCreditCardResponse

class CustomersController(BaseController):

    """A Controller to access Endpoints in the mundiapilib API."""


    def get_addresses(self,
                      customer_id):
        """Does a GET request to /customers/{customer_id}/addresses.

        Gets all adressess from a customer

        Args:
            customer_id (string): Customer id

        Returns:
            ListAddressesResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListAddressesResponse.from_dictionary)

    def get_credit_cards(self,
                         customer_id):
        """Does a GET request to /customers/{customer_id}/credit_cards.

        Get all credit cards from a customer

        Args:
            customer_id (string): Customer Id

        Returns:
            ListCardsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/credit_cards'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListCardsResponse.from_dictionary)

    def get_customers(self):
        """Does a GET request to /customers.

        Get all Customers

        Returns:
            ListCustomersResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListCustomersResponse.from_dictionary)

    def create_customer(self,
                        request):
        """Does a POST request to /customers.

        Creates a new customer

        Args:
            request (CreateCustomerRequest): Request for creating a customer

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)

    def get_customer(self,
                     customer_id):
        """Does a GET request to /customers/{customer_id}.

        Get a customer

        Args:
            customer_id (string): Customer Id

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)

    def update_address(self,
                       customer_id,
                       address_id,
                       request):
        """Does a PUT request to /customers/{customer_id}/addresses/{address_id}.

        Updates an address

        Args:
            customer_id (string): Customer Id
            address_id (string): Address Id
            request (UpdateAddressRequest): Request for updating an address

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def update_credit_card(self,
                           customer_id,
                           card_id,
                           request):
        """Does a PUT request to /customers/{customer_id}/credit_cards/{card_id}.

        Updates a credit card

        Args:
            customer_id (string): Customer Id
            card_id (string): Credit card id
            request (UpdateCreditCardRequest): Request for updating a credit
                card

        Returns:
            GetCreditCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/credit_cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCreditCardResponse.from_dictionary)

    def get_address(self,
                    customer_id,
                    address_id):
        """Does a GET request to /customers/{customer_id}/addresses/{address_id}.

        Get a customer's address

        Args:
            customer_id (string): Customer id
            address_id (string): Address Id

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def delete_address(self,
                       customer_id,
                       address_id):
        """Does a DELETE request to /customers/{customer_id}/addresses/{address_id}.

        Delete a Customer's address

        Args:
            customer_id (string): Customer Id
            address_id (string): Address Id

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def delete_credit_card(self,
                           customer_id,
                           card_id):
        """Does a DELETE request to /customers/{customer_id}/credit_cards/{card_id}.

        Delete a customer's credit card

        Args:
            customer_id (string): Customer Id
            card_id (string): Card Id

        Returns:
            GetCreditCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/credit_cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCreditCardResponse.from_dictionary)

    def create_address(self,
                       customer_id,
                       request):
        """Does a POST request to /customers/{customer_id}/addresses.

        Creates a new address for a customer

        Args:
            customer_id (string): Customer Id
            request (CreateAddressRequest): Request for creating an address

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def get_credit_card(self,
                        customer_id,
                        card_id):
        """Does a GET request to /customers/{customer_id}/credit_cards/{card_id}.

        Get a customer's credit card

        Args:
            customer_id (string): Customer id
            card_id (string): Card id

        Returns:
            GetCreditCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/credit_cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCreditCardResponse.from_dictionary)

    def create_credit_card(self,
                           customer_id,
                           request):
        """Does a POST request to /customers/{customer_id}/credit_cards.

        Creates a new credit card for a customer

        Args:
            customer_id (string): Customer id
            request (CreateCreditCardRequest): Request for creating a credit
                card

        Returns:
            GetCreditCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/credit_cards'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCreditCardResponse.from_dictionary)

    def update_customer(self,
                        customer_id,
                        request):
        """Does a PUT request to /customers/{customer_id}.

        Updates a customer

        Args:
            customer_id (string): Customer id
            request (UpdateCustomerRequest): Request for updating a customer

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)
