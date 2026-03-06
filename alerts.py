from api_client import get_curr_price

def list_alerts(alerts_data):
    print("Active alerts:")
    print("-" * 15)
    for alert in alerts_data:
        print(f"{alert["ticker"]} {alert["condition"]} {alert["threshold"]}")

def remove_alerts(alerts_data, ticker):
    original = len(alerts_data)
    keep_alerts = [alert for alert in alerts_data if alert["ticker"] != ticker]
    if len(keep_alerts) < original:
        print(f"Alert for {ticker} removed")
    else:
        print(f"No alert found for {ticker}")
    return keep_alerts


# add_alert(alerts_data, ticker, condition, threshold)

# check_alert(alert)