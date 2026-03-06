# handles file reading/writing 
import json

def load_portfolio():
    try:
        with open('data/portfolio.json','r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: The file 'portfolio.json' was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return {}

def save_portfolio(portfolio_data):
    with open("data/portfolio.json","w") as f:
        json.dump(portfolio_data, f, indent=4)

def load_alerts():
    try:
        with open('data/alerts.json','r') as file:
            alerts = json.load(file)
            return alerts
    except FileNotFoundError:
        print("Error: The file 'alerts.json' was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return {}

def save_alerts(alerts):
    with open("data/alerts.json","w") as f:
        json.dump(alerts, f, indent=4)