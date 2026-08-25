from django.shortcuts import render


def dashboard(request):
    return render(request, "currency/index.html", context={"test": range(10)})
