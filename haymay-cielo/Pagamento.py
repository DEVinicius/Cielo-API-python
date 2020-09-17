import requests, json

class Pagamento():
    
    def creditCard(self, merchantOrderId, CustomerName, Amount, Installments, CardNumber, CardHolder, ExpirationDate, SecurityCode, Brand):
        header = {
            "Content-Type" : "application/json",
            "MerchantId" : 'e95add03-2cfe-4a63-9573-239eeebcdeb6',
            "MerchantKey" : "BSCWMSQLHMKBFYIMIEEKNJKPNARGMCWFVKVVYHJG"
        }

        url = "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/"
        json_data = {
            "MerchantOrderId": merchantOrderId,
            "Customer": {
                "Name": CustomerName
            },
            "Payment":{
                "Type":"CreditCard",
                "Amount": Amount,
                "Installments": Installments,
                "CreditCard":{
                    "CardNumber": CardNumber,
                    "Holder": CardHolder,
                    "ExpirationDate": ExpirationDate,
                    "SecurityCode": SecurityCode,
                    "Brand": Brand
                }
            }
        }

        request = requests.post(url, headers = header, json = json_data)
        print(request.text)

    def BankSlip(self, MerchantOrderId, CustomerName, CustomerZipCode, CustomerCountry, CustomerState, CustomerCity, CustomerDistrict, CustomerStreet, CustomerNumber, CustomerComplement, PaymentAmount, PaymentAddress, BankSlipNumber, BankSlipExpirationDate, CompanyName):
        header = {
            "Content-Type" : "application/json",
            "MerchantId" : 'e95add03-2cfe-4a63-9573-239eeebcdeb6',
            "MerchantKey" : "BSCWMSQLHMKBFYIMIEEKNJKPNARGMCWFVKVVYHJG"
        }

        url = "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/"
        json = {
            "MerchantOrderId": MerchantOrderId,
            "Customer": 
            {
                "Name": CustomerName,
                "Address":
                {
                    "Street" : CustomerStreet,
                    "Number" : CustomerNumber,
                    "Complement" : CustomerComplement,
                    "ZipCode" : CustomerZipCode,
                    "District" : CustomerDistrict,
                    "City" : CustomerCity,
                    "State" : CustomerState,
                    "Country" : CustomerCountry
                }
            },
            "Payment":
            {
                "Type" : "Boleto",
                "Amount" : PaymentAmount,
                "Provider" : "Simulado",
                "Address" : PaymentAddress,
                "BoletoNumber" : BankSlipNumber,
                "Assignor" : CompanyName,
                "ExpirationDate" : BankSlipExpirationDate
            }
        }
