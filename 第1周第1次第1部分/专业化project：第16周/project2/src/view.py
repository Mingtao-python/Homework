def view_watchlist(watchlist):
    """View all companies in the watchlist."""
    print("\nYour Watchlist:")
    if not watchlist:
        print("Watchlist is empty.")
    else:
        for idx, company in enumerate(watchlist, start=1):
            print(f"{idx}. {company}")
    print()
