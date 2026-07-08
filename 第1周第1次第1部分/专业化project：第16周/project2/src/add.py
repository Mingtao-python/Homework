def add_company(watchlist):
    """Add a company to the watchlist."""
    name = input("Enter company name: ").strip()
    if name:
        watchlist.append(name)
        print(f"Added: {name}")
    else:
        print("Company name cannot be empty.")
