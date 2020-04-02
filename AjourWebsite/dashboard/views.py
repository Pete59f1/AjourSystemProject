from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    return render(request, 'register.html')
