from api_client import get_curr_price
from storage import *
from portfolio import *

price, error = get_curr_price("AAPL")

if error:
    print(f"Error: {error}")
else:
    print(f"The current price of AAPL is ${price:.2f}")

portfolio = load_portfolio()
display_portfolio(portfolio)

curr_val = calculate_portfolio_value(portfolio)
print(f"{curr_val:.2f}")