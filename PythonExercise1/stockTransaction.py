#Stock transaction program
print("---------------------INPUTS----------------------\n")
amountShares    = float(input("Input the amount of shares that you purchased: ")) 
PriceAtPurchase = float(input("Input how much you bought the stocks for: "))
BuyCom          = float(input("Input broker buying commission percent: "))/100
PriceAtSale     = float(input("Input how much each stock was sold for on sale: "))
SaleCom         = float(input("Input broker selling commission percent: "))/100
buyPrice        = amountShares*PriceAtPurchase
salePrice       = amountShares*PriceAtSale

Profit          = (salePrice - salePrice * SaleCom) - (buyPrice + buyPrice * BuyCom)
print("\n---------------------OUTPUTS---------------------")
print(f"""
Amount payed in total:  {"{:.2f}".format(amountShares*PriceAtPurchase)}
Broker Commisssion on intial payment: {"{:.2f}".format(BuyCom*(amountShares*PriceAtPurchase))}
Amount Stock Sold for: {"{:.2f}".format(amountShares*PriceAtSale)}
Broker Commission on sale: {"{:.2f}".format(SaleCom*(amountShares*PriceAtSale))}
Profit made on sale: {"{:.2f}".format(Profit)}
      """)
input("Press any key to quit: ")
