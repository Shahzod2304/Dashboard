from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home, name='home'),
    path('page-404/', Page_404, name='page_404'),
    path('account/', Account, name='account'),
    path('chart/', Chart, name='chart'),
    path('docs/', Docs, name='docs'),
    path('help/', Help, name='help'),
    path('login/', Login, name='login'),
    path('notifications/', Notifications, name='notifications'),
    path('orders/', Orders, name='orders'),
    path('reset-password/', Reset_Password, name='reset_password'),
    path('settings/', Settings, name='settings'),
    path('signup/', Signup, name='signup'),
    
]
