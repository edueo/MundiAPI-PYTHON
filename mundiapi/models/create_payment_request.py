# -*- coding: utf-8 -*-

"""
    mundiapi.models.create_payment_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_credit_card_payment_request
import mundiapi.models.create_boleto_payment_request
import mundiapi.models.create_voucher_payment_request
import mundiapi.models.create_bank_transfer_payment_request

class CreatePaymentRequest(object):

    """Implementation of the 'CreatePaymentRequest' model.

    Payment data

    Attributes:
        payment_method (string): Payment method
        credit_card (CreateCreditCardPaymentRequest): Settings for credit card
            payment
        boleto (CreateBoletoPaymentRequest): Settings for boleto payment
        currency (string): Currency. Must be informed using 3 characters
        voucher (CreateVoucherPaymentRequest): Settings for voucher payment
        bank_transfer (CreateBankTransferPaymentRequest): Settings for bank
            transfer payment
        gateway_affiliation_id (string): Gateway affiliation code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_method" : "payment_method",
        "credit_card" : "credit_card",
        "boleto" : "boleto",
        "currency" : "currency",
        "voucher" : "voucher",
        "bank_transfer" : "bank_transfer",
        "gateway_affiliation_id" : "gateway_affiliation_id"
    }

    def __init__(self,
                 payment_method=None,
                 credit_card=None,
                 boleto=None,
                 currency=None,
                 voucher=None,
                 bank_transfer=None,
                 gateway_affiliation_id=None):
        """Constructor for the CreatePaymentRequest class"""

        # Initialize members of the class
        self.payment_method = payment_method
        self.credit_card = credit_card
        self.boleto = boleto
        self.currency = currency
        self.voucher = voucher
        self.bank_transfer = bank_transfer
        self.gateway_affiliation_id = gateway_affiliation_id


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
        credit_card = mundiapi.models.create_credit_card_payment_request.CreateCreditCardPaymentRequest.from_dictionary(dictionary.get("credit_card")) if dictionary.get("credit_card") else None
        boleto = mundiapi.models.create_boleto_payment_request.CreateBoletoPaymentRequest.from_dictionary(dictionary.get("boleto")) if dictionary.get("boleto") else None
        currency = dictionary.get("currency")
        voucher = mundiapi.models.create_voucher_payment_request.CreateVoucherPaymentRequest.from_dictionary(dictionary.get("voucher")) if dictionary.get("voucher") else None
        bank_transfer = mundiapi.models.create_bank_transfer_payment_request.CreateBankTransferPaymentRequest.from_dictionary(dictionary.get("bank_transfer")) if dictionary.get("bank_transfer") else None
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id")

        # Return an object of this model
        return cls(payment_method,
                   credit_card,
                   boleto,
                   currency,
                   voucher,
                   bank_transfer,
                   gateway_affiliation_id)


