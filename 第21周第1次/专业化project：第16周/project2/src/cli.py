from .load import load_watchlist
from .save import save_watchlist
from .add import add_company
from .delete import delete_company
from .view import view_watchlist


def run_cli():
    """Run the watchlist command-line interface."""
    watchlist = load_watchlist()

    while True:
        print("\n--- Watchlist CLI ---")
        print("1 Add Company")
        print("2 Delete Company")
        print("3 View Watchlist")
        print("4 Save")
        print("5 Load")
        print("0 Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_company(watchlist)
        elif choice == "2":
            delete_company(watchlist)
        elif choice == "3":
            view_watchlist(watchlist)
        elif choice == "4":
            save_watchlist(watchlist)
            print("Saved.")
        elif choice == "5":
            watchlist = load_watchlist()
            print("Loaded.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
