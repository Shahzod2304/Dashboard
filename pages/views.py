from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Page_404(request):
    return render(request, '404.html')

def Account(request):
    return render(request, 'account.html')

def Chart(request):
    return render(request, 'charts.html')

def Docs(request):
    return render(request, 'docs.html')

def Help(request):
    return render(request, 'help.html')

def Login(request):
    return render(request, 'login.html')

def Notifications(request):
    return render(request, 'notifications.html')

def Orders(request):
    return render(request, 'orders.html')

def Reset_Password(request):
    return render(request, 'reset-password.html')

def Settings(request):
    return render(request, 'settings.html')

def Signup(request):
    return render(request, 'signup.html')
