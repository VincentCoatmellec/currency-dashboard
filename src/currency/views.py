from django.shortcuts import render, redirect

import api


def redirect_home(request):
    return redirect("home", days_range=30, currencies="USD")


def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(
        currencies=currencies.split(","), days=days_range)
    page_label = {7: "Week", 30: "Month", 90: "Quarter",
                  365: "Year"}.get(days_range, "Custom")

    return render(request, "currency/index.html", context={"data": rates,
                                                           "days_labels": days,
                                                           "currencies": currencies,
                                                           "page_label": page_label})
