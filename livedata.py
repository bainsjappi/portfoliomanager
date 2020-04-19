from bsedata.bse import BSE as BSE1

def getTicker():
    tkr = input("Enter the Stock Ticker")
    q = getStockQuoteBse(tkr)
    print(q)


def getStockQuoteBse(symbol):
    b = BSE1()
    if symbol =="":
        return
    else:
        q=b.getQuote(symbol)
        #return "company=" + q["companyName"],"high=" + q["dayHigh"]
        return q["companyName"],  q["previousOpen"] , q["dayHigh"], q["dayLow"], q["currentValue"]
        
