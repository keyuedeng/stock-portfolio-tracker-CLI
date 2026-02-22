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
    results = {}

    for ticker, purchases in portfolio_data.items():
        total_shares = 0
        curr_val = 0
        cost_basis = 0

        for purchase in purchases:
            total_shares += purchase['quantity']
            cost_basis += purchase['quantity'] * purchase['purchasePrice']

        price, error = get_curr_price(ticker)
        if error:
            print(f"Warning: Could not fetch price for {ticker}: {error}")
            continue

        curr_val += total_shares * price
        pnl_dollar = curr_val - cost_basis
        pnl_percent = 100 * pnl_dollar/cost_basis

        results[ticker] = {
            "total_shares": total_shares,
            "cost_basis": cost_basis,
            "current_value": curr_val,
            "pnl_dollar": pnl_dollar,
            "pnl_percent": pnl_percent
        }
    
    return results
