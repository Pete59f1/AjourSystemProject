from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
import requests
# from AjourWebsite.accounts.MachineLearning import ML


def indexView(request):
    return render(request, 'index.html')


@login_required(login_url='login_url')
def dashboardView(request):
    data = requests.get('https://cr3d0pygtd.execute-api.eu-north-1.amazonaws.com/Prod/api/Values?fbclid=IwAR3IAjkZiGBTnVvBhWaT6cMup2YYfsrxq8sqJ_s874Lc9DX3Va-_Db-r9C8')
    datajson = data.json()
    return render(request, 'dashboard.html',
                  {
                      'data': datajson,
                      # 'bla': datajson['bla']
                  })


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


# Not being used anymore
def SQLInjection(request):
    # param1 = request.POST.get("userName")
    query = "SELECT * FROM auth_user" # WHERE username = '%s'" % param1

    # Show the table names
    # tables = connection.introspection.table_names()

    with connection.cursor() as cursor:
        cursor.execute(query)
        userNames = cursor.fetchall()

    # The right way to write raw sql in django. This is more secure against sql injection
    # user = User.objects.raw('SELECT * FROM Users WHERE USERNAME = %s', [param1])

    # Links used
    # https://stackoverflow.com/questions/5931586/raw-sql-queries-in-django-views
    # https://docs.djangoproject.com/en/3.0/topics/db/sql/

    return render(request, "SQLInjection.html", {"data1": userNames})
