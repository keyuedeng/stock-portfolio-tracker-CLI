from api_client import get_curr_price

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

def calculate_portfolio_value(portfolio_data):
    curr_val = 0
    for ticker, purchases in portfolio_data.items():
        ticker_quantity = 0
        for purchase in purchases:
            ticker_quantity += purchase['quantity']
        # call api client
        print(f"fetchign price for {ticker}...")
        price, error = get_curr_price(ticker)
        print(f"result: price = {price}, error={error}")
        curr_val += ticker_quantity * price
    return curr_val


