from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies: list[str], days: int = 30) -> tuple[list[str], dict[str, list[float]]]:
    """Get historical exchange rates for a list of currencies.

    Args:
        currencies (list[str]): List of currency codes.
        days (int, optional): Number of days of history to retrieve. Defaults to 30.

    Returns:
        tuple[list[str], dict[str, list[float]]]: A tuple containing the list of dates and a dictionary of exchange rates.
    """
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    # Create the query URL for the API request
    symbols = ','.join(currencies)
    query = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}"

    # Make the API request and handle the response
    r = requests.get(query)
    if not r or not r.json():
        return [], {}
    api_rates = r.json().get("rates")

    # Initialize a dictionary to hold the exchange rates for each currency
    all_rates = {currency: [] for currency in currencies}

    # Sort the dates and populate the exchange rates for each currency
    all_days = sorted(api_rates.keys())
    for each_day in all_days:
        for currency, rate in api_rates[each_day].items():
            all_rates[currency].append(rate)

    return all_days, all_rates


if __name__ == "__main__":
    days, rates = get_rates(currencies=["USD", "CAD"])
    pprint(days)
    pprint(rates)
