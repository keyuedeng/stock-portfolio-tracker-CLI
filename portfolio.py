def display_portfolio(portfolio_data):
    print("Portfolio Holdings:")
    print("---"*15)
    for ticker,data in portfolio_data.items():
        print(f"{ticker}:")
        for purchase in data:
            print(f"\t{purchase['purchaseDate']}: {purchase['quantity']} shares @ ${purchase['purchasePrice']:.2f}")

def add_holding(portfolio_data, ticker, date, quantity, price):
    if ticker in portfolio_data:
        portfolio_data[ticker].append({
            "purchaseDate":date,
            "quantity": quantity,
            "purchasePrice": price
        })
    else:
        portfolio_data[ticker] = [{
            "purchaseDate":date,
            "quantity": quantity,
            "purchasePrice": price
        }]