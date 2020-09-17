import requests, json

class Pagamento():

    def __init__(self, merchantOrderId, CustomerName, Amount, Installments, CardNumber, CardHolder, ExpirationDate, SecurityCode, Brand):
        self.merchantOrderId = merchantOrderId
        self.CustomerName = CustomerName
        self.Amount = Amount
        self.Installments = Installments
        self.CardNumber = CardNumber
        self.CardHolder = CardHolder
        self.ExpirationDate = ExpirationDate
        self.SecurityCode = SecurityCode
        self.Brand = Brand
    
    def creditCard(self, ):
        header = {
            "Content-Type" : "application/json",
            "MerchantId" : 'e95add03-2cfe-4a63-9573-239eeebcdeb6',
            "MerchantKey" : "BSCWMSQLHMKBFYIMIEEKNJKPNARGMCWFVKVVYHJG"
        }

        url = "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/"
        json_data = {
            "MerchantOrderId": self.merchantOrderId,
            "Customer": {
                "Name": self.CustomerName
            },
            "Payment":{
                "Type":"CreditCard",
                "Amount": self.Amount,
                "Installments": self.Installments,
                "CreditCard":{
                    "CardNumber": self.CardNumber,
                    "Holder": self.CardHolder,
                    "ExpirationDate": self.ExpirationDate,
                    "SecurityCode": self.SecurityCode,
                    "Brand": self.Brand
                }
            }
        }

        request = requests.post(url, headers = header, json = json_data)
        print(request)
