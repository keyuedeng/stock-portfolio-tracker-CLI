from api_client import get_curr_price
from storage import *
from portfolio import *


portfolio = load_portfolio()

portfolio_value = calculate_portfolio_value(portfolio)
display_portfolio_summary(portfolio_value)