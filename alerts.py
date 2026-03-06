from api_client import get_curr_price

def list_alerts(alerts_data):
    print("Active alerts:")
    print("-" * 15)
    for alert in alerts_data:
        print(f"{alert["ticker"]} {alert["condition"]} {alert["threshold"]}")


# remove_alerts(alerts_data, ticker)

# add_alert(alerts_data, ticker, condition, threshold)

# check_alert(alert)