from api_client import get_curr_price

price, error = get_curr_price("AAPL")

if error:
    print(f"Error: {error}")
else:
    print(f"The current price of AAPL is ${price:.2f}")