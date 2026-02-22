import yfinance as yf

def get_curr_price(ticker):
    try:
        stock = yf.Ticker(ticker)

        # check if data exists 
        if not stock.info:
            return None, "Could not fetch data for ticker"

        price = stock.info.get('currentPrice') or \
                stock.info.get('regularMarketPrice') or \
                stock.info.get('previousClose')
        return price, None # returns in format (price, error)
    
    except KeyError: #keyerror is when you try to access a dicitonary key that doesn't exist
        return None, f"Invalid ticker: {ticker}"
    except Exception as e: #if error happens, catch it and call it 'e'
        return None, f"Error fetching price: {str(e)}"






