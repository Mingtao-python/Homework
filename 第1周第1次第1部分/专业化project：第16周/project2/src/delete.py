def delete_company(watchlist):
    """Delete a company from the watchlist."""
    name = input("Enter company name to delete: ").strip()
    if name in watchlist:
        watchlist.remove(name)
        print(f"Deleted: {name}")
    else:
        print("Company not found.")
