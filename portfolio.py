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

def remove_holding(portfolio_data, ticker):
    if ticker in portfolio_data:
        del portfolio_data[ticker]
        print(f"Removed {ticker} from portfolio")
    else:
        print(f"{ticker} not in portfolio")


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

def display_portfolio_summary(portfolio_value):
    total_cost_basis = 0
    total_curr_val = 0

    for ticker, data in portfolio_value.items():
        total_cost_basis += data['cost_basis']
        total_curr_val += data['current_value']

        # per ticker data
        print(f"{ticker}:")
        
        print(f"\tTotal Shares: {data['total_shares']}")
        print(f"\tCost basis: ${data['cost_basis']:.2f}")
        print(f"\tCurrent Value: ${data['current_value']:.2f}")
        if data["pnl_dollar"] < 0:
            print(f"\tP&L: ${data['pnl_dollar']:.2f} ({data['pnl_percent']:.2f}%)")
        else:
            print(f"\tP&L: +${data['pnl_dollar']:.2f} (+{data['pnl_percent']:.2f}%)")

    # calculate total pnl
    total_pnl_dollar = total_curr_val - total_cost_basis
    total_pnl_percent = 100 * total_pnl_dollar/total_cost_basis

    print("\n")
    print("-" * 30)
    print("Total Portfolio:")
    print(f"\tCost Basis: ${total_cost_basis:.2f}")
    print(f"\tCurrent Value: ${total_curr_val:.2f}")
    if total_pnl_dollar < 0:
        print(f"\tTotal P&L: ${total_pnl_dollar:.2f} ({total_pnl_percent:.2f}%)")
    else:
        print(f"\tTotal P&L: +${total_pnl_dollar:.2f} (+{total_pnl_percent:.2f}%)")
