from api_client import get_curr_price
from storage import load_portfolio
from portfolio import display_portfolio

price, error = get_curr_price("AAPL")

if error:
    print(f"Error: {error}")
else:
    print(f"The current price of AAPL is ${price:.2f}")

portfolio = load_portfolio()
display_portfolio(portfolio)
