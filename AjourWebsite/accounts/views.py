from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection


def indexView(request):
    return render(request, 'index.html')


@login_required(login_url='login_url')
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url="login_url")
def mlPrediction(request):
    param1 = request.POST.get("degreesValue")
    param2 = request.POST.get("weatherValue")
    prediction = "HEJJJE " + param1 + param2

    return render(request, "dashboard.html", {"data1": prediction})


def SQLInjection(request):
    param1 = request.POST.get("userName")
    query = "SELECT password FROM User WHERE username = '%s'" % param1
    user = User.objects.raw(query)

    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM users")
        row = cursor.fetchone()
        print(row)

    # The right way to write raw sql in django. This is more secure against sql injection
    # user = User.objects.raw('SELECT * FROM Users WHERE USERNAME = %s', [param1])

    return render(request, "SQLInjection.html", {"data1": user})
