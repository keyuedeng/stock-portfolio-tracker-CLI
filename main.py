from api_client import get_curr_price
from storage import *
from portfolio import *
from alerts import *

print("Welcome to your Portfolio Tracker")
print("Commands: view, add [ticker] [qty] [price] [date], remove [ticker]")
print("Type 'exit' to exit")
print("-" * 60)

while True:
    user_input = input("> ").strip()

    if not user_input:
        continue

    # split input into parts
    parts = user_input.split()
    command = parts[0].lower()
    
    if command == "exit":
        print("Goodbye!")
        break

    elif command == "list":
        portfolio = load_portfolio()
        list_holdings(portfolio)
    
    elif command == "view":
        portfolio = load_portfolio()
        portfolio_value = calculate_portfolio_value(portfolio)
        display_portfolio_summary(portfolio_value)
    
    elif command == "add":
        try: 
            if len(parts) < 5:
                print("Usage: add [ticker] [qty] [price] [date]")
            else:
                ticker = parts[1]
                quantity = int(parts[2])
                price = float(parts[3])
                date = parts[4]

                portfolio = load_portfolio()
                add_holding(portfolio, ticker, date, quantity, price)
                save_portfolio(portfolio)
                print(f"Added {quantity} shares of {ticker}")
        except IndexError:
            print("Usage: add [ticker] [qty] [price] [date]")
        except ValueError:
            print("Error: quantity must be a number, price must be a number")
        
    elif command == "remove":
        if len(parts) != 2:
            print("Usage: remove [ticker]")
        else:
            ticker = parts[1].upper()

            portfolio = load_portfolio()
            remove_holding(portfolio, ticker)
            save_portfolio(portfolio)
    
    elif command == "alert":
        if len(parts) < 2:
            print("Usage: alert [list|add|remove|check]")
        elif parts[1] == "list":
            alerts_data = load_alerts()
            list_alerts(alerts_data)
        elif parts[1] == "remove": 
            if len(parts) < 3:
                print("Usage: alert remove [ticker]")
            else:
                alerts_data = load_alerts()
                alerts_data = remove_alerts(alerts_data, parts[2].upper())
                save_alerts(alerts_data)

    else:
        print("Unknown command")

