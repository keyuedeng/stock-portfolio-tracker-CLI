def display_portfolio(portfolio_data):
    print("Portfolio Holdings:")
    print("---"*15)
    for ticker,data in portfolio_data.items():
        print(f"{ticker}:")
        for purchase in data:
            print(f"\t{purchase['purchaseDate']}: {purchase['quantity']} shares @ ${purchase['purchasePrice']:.2f}")
