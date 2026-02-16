import yfinance as yf

def get_curr_price(ticker):
    try:
        stock = yf.Ticker(ticker)

        # check if data exists 
        if not stock.info:
            return None, "Could not fetch data for ticker"
        
        # check if price exists in data
        if 'currentPrice' not in stock.info:
            return None, "Price not available for this ticker"

        price = stock.info.get('currentPrice')
        return price, None # returns in format (price, error)
    
    except KeyError: #keyerror is when you try to access a dicitonary key that doesn't exist
        return None, f"Invalid ticker: {ticker}"
    except Exception as e: #if error happens, catch it and call it 'e'
        return None, f"Error fetching price: {str(e)}"






