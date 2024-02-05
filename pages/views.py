from django.shortcuts import render
from .models import * 
import pandas as pd

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
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        # Pandas orqali Excel faylini o'qish
        df = pd.read_excel(excel_file)
        # Modelga yuklash
        for index, row in df.iterrows():
            Excel_file.objects.create(
                Year=row['Year'],
                Industry_aggregation_NZSIOC=row['Industry_aggregation_NZSIOC'],
                Industry_code_NZSIOC=row['Industry_code_NZSIOC'],
                Industry_name_NZSIOC=row['Industry_name_NZSIOC'],
                Units=row['Units'],
                Variable_code=row['Variable_code'],
                Variable_name=row['Variable_name'],
                Variable_category=row['Variable_category'],
                Value=row['Value'],
                Industry_code_ANZSIC06=row['Industry_code_ANZSIC06'],
                # Qo'shimcha maydonlar...
            )
    return render(request, 'docs.html')

def Help(request):
    return render(request, 'help.html')

def Login(request):
    return render(request, 'login.html')

def Notifications(request):
    return render(request, 'notifications.html')

def Orders(request):
    

    my_model_data = Excel_file.objects.all()
    context = {
        'my_model_data': my_model_data,
    }

    return render(request, 'orders.html',  context)

def Reset_Password(request):
    return render(request, 'reset-password.html')

def Settings(request):
    return render(request, 'settings.html')

def Signup(request):
    return render(request, 'signup.html')
