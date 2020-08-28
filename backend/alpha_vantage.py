import urllib.request as request
from fastapi import HTTPException
import json

class AlphaVantage:

    def __init__(self):
        self.apiKey = ""
        self.baseUrl = "https://www.alphavantage.co/query?apikey="+self.apiKey

    def quotation(self, symbol):
        
        url = self.baseUrl + "&function=GLOBAL_QUOTE"+"&symbol="+symbol
        
        with request.urlopen(url) as response:
            if response.getcode() == 200:
                source = response.read()
                data = json.loads(source)

                if data == {'Global Quote': {}} or data == {}:
                    # Here, if the API returns "nothing" it will raise an Exception with "Not found" status code
                    raise HTTPException(status_code=404, detail="Looks like this symbol doesn't exists... :/")
                
                else:
                    symbol = data["Global Quote"]["01. symbol"]
                    price = float(data["Global Quote"]["05. price"])
                    
                    # Here will return only the nescessary for our frontend
                    return {"symbol": symbol, "price": price}

            else:
                # If things go bad XD
                return {"error":"Something unexpected happened... :/"}
            