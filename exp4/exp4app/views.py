from django.shortcuts import render

def map(request):
    return render(request, 'map.html')

def chromepet(request):
    return render(request, 'chromepet.html')

def copperkitchen(request):
    return render(request, 'copperkitchen.html')

def hotelgrandpalace(request):
    return render(request, 'hotelgrandpalace.html')

def nandhanapalace(request):
    return render(request, 'nandhanapalace.html')

def temple(request):
    return render(request, 'temple.html')
